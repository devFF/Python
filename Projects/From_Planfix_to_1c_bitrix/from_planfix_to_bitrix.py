import requests
import os
import csv
import codecs
from requests.structures import CaseInsensitiveDict
import xmltodict
import json
import io


class API_reader():
    def __init__(self, run: bool, link: str, key1: str, key2: str, auth_xml_file: str):
        # Запросы через сессию, чтобы сохранить авторизацию
        self.sess = requests.Session()
        self.link, self.key1, self.key2 = link, key1, key2
        # Прописываем шапку
        self.headers = CaseInsensitiveDict()
        self.headers["Content-Type"] = "application/xml"
        self.headers["Accept"] = "application/xml"
        self.get_sid(run=run, auth_xml_file=auth_xml_file)

    def get_sid(self, run: bool, auth_xml_file: str):
        if not run: return None
        # Авторизация для получения sid-ключа
        with open(os.path.join(os.getcwd(), 'input', auth_xml_file), 'r') as r:
            auth_data = r.read()
        # POST-запрос на авторизацию
        response = self.sess.post(self.link, headers=self.headers, data=auth_data, auth=(self.key1, self.key2))
        if 'status="ok"' not in response.text:
            print('Ошибка авторизации, ответ сервера: ', response.text)

        # Парсим ответ сервера и вытаскиваем sid-ключ
        self.sid = response.text.split()[-1].replace('status="ok"><sid>', '').replace('</sid></response>', '')
        print('SID-key: {}'.format(self.sid))

    def export_data(self, run: bool, xml_file: str, page: int):
        if not run: return None
        # Создаем xml-запрос с sid-ключом для получения списка задач
        with open(os.path.join(os.getcwd(), 'input', xml_file), 'r') as r:
            data = r.read().replace('setsid', str(self.sid)).replace('<pageCurrent>1</pageCurrent>',
                                                                     '<pageCurrent>{}</pageCurrent>'.format(page))

        # Отправляем post-запрос для получения списка задач
        response = self.sess.post(self.link, headers=self.headers, data=data, auth=(self.key1, self.key2))
        if 'status="ok"' not in response.text:
            print('Ошибка запроса, ответ сервера : ', response.text)
        with open(os.path.join(os.getcwd(), 'response', f'response_{xml_file}'), 'w') as w:
            w.write(response.text)


class Parser():
    def __init__(self, out_csv_file: str):
        self.task_title_list, self.active_from_list = [], []
        self.IE_CODE_list, self.executors_list = [], []
        self.description_list, self.project_list, self.status_list = [], [], []
        self.run_parse()
        self.write_new_csv(out_csv_file='full_csv.csv')

    def run_parse(self):
        task_limit = 100
        is_limit = False
        counter = 1
        while not is_limit:
            if counter > 1:
                API.export_data(run=True, xml_file='get_tasks.txt', page=counter)
            dict_to_write = self.xml_to_dict('response_get_tasks.txt')
            number_of_tasks = self.parse(dict_to_write=dict_to_write, page=counter)
            if number_of_tasks < task_limit:
                is_limit = True
                if counter == 1:
                    print('Парсинг завершен. Получено {} задач.'.format(number_of_tasks))
                else:
                    print('Парсинг завершен. Получено {} задач.'.format(task_limit * counter + number_of_tasks))
            counter += 1

    def read_csv(self, csv_file):
        """Чтение основного csv-файла"""
        file = codecs.open(os.path.join(os.getcwd(), 'import', csv_file), encoding='utf-8', mode='r')
        self.current_csv = list(csv.reader(file))
        self.current_csv[0][0] = self.current_csv[0][0].replace('\ufeff', '')
        print(self.current_csv)


    def write_new_csv(self, out_csv_file):
        data = [
            'IE_NAME;IE_ACTIVE;IE_ACTIVE_FROM;IE_CODE;IE_SORT;IP_PROP381;IP_PROP383;IP_PROP382;IP_PROP385;IP_PROP384;IC_GROUP0']
        for i in range(len(self.task_title_list)):
            row_str = '{IE_NAME};{IE_ACTIVE};{IE_ACTIVE_FROM};{IE_CODE};{IE_SORT};{IP_PROP381};{IP_PROP383};' \
                      '{IP_PROP382};{IP_PROP385};{IP_PROP384};{IC_GROUP0}'.format(
                IE_NAME=self.task_title_list[i],
                IE_ACTIVE='Y',
                IE_ACTIVE_FROM=self.active_from_list[i],
                IE_CODE=self.IE_CODE_list[i],
                IE_SORT='500',
                IP_PROP381=self.task_title_list[i],
                IP_PROP383=self.executors_list[i],
                IP_PROP382=self.description_list[i],
                IP_PROP385=self.project_list[i],
                IP_PROP384=self.status_list[i],
                IC_GROUP0=self.project_list[i])
            data.append(row_str)

        with codecs.open(os.path.join(os.getcwd(), 'import', out_csv_file), 'w', encoding='utf8') as file:
            total_string = ''
            for i in range(len(self.task_title_list)):
                total_string += data[i] + '\n'
            file.write(total_string)

    def parse(self, dict_to_write, page):
        del_list = ['importance', 'statusSet', 'parent']
        try:
            print(len(dict_to_write['response']['tasks']['task']))
        except KeyError:
            print("Список задач на странице №{} равен нулю. Конец работы программы.".format(page))
            return 0

        for i in range(1, len(dict_to_write['response']['tasks']['task'])):
            executors = str()
            for j in range(len(del_list)):
                del dict_to_write['response']['tasks']['task'][i][del_list[j]]
            self.task_title_list.append(dict_to_write['response']['tasks']['task'][i]['title'])
            self.IE_CODE_list.append('Taks{}'.format(i))
            self.project_list.append(dict_to_write['response']['tasks']['task'][i]['project']['title'])
            self.active_from_list.append(dict_to_write['response']['tasks']['task'][i]['beginDateTime'])
            self.status_list.append(dict_to_write['response']['tasks']['task'][i]['status'])
            self.description_list.append(dict_to_write['response']['tasks']['task'][i]['description'])
            try:
                if isinstance(dict_to_write['response']['tasks']['task'][i]['workers']['users']['user'], list):
                    for j in range(len(dict_to_write['response']['tasks']['task'][i]['workers']['users']['user'])):
                        executor = (
                            dict_to_write['response']['tasks']['task'][i]['workers']['users']['user'][j]['name'])
                        if j == len(dict_to_write['response']['tasks']['task'][i]['workers']['users']['user']) - 1:
                            executors += executor
                        else:
                            executors += executor + ', '
                    self.executors_list.append(executors)
                else:
                    self.executors_list.append(
                        dict_to_write['response']['tasks']['task'][i]['workers']['users']['user']['name'])
            except:
                self.executors_list.append(
                    dict_to_write['response']['tasks']['task'][i]['owner']['name'])

        # Обработка статуса
        for i in range(len(self.status_list)):
            if self.status_list[i] == '3':
                self.status_list[i] = 'Выполнено'
            else:
                self.status_list[i] = 'В работе'

        # Обработка описания
        for i in range(len(self.description_list)):
            if self.description_list[i] is None:
                self.description_list[i] = 'Без описания'
            else:
                self.description_list[i] = self.description_list[i].replace('<p>', '').replace('</p>', '')

        # Обработка проекта
        for i in range(len(self.project_list)):
            if self.project_list[i] is None:
                self.project_list[i] = 'Не указан'

        # Обработка даты: из DD-MM-YYYY HH:MM -> DD.MM.YYYY HH:MM:SS
        for i in range(len(self.active_from_list)):
            self.active_from_list[i] = self.active_from_list[i].replace('-', '.') + ':00'

        return len(dict_to_write['response']['tasks']['task'])

    def xml_to_dict(self, csv_file):
        with codecs.open(os.path.join(os.getcwd(), 'response', csv_file), 'r', encoding='cp1251') as xml_file:
            xml_file = xml_file.read()
            o = xmltodict.parse(xml_file)
            output_dict = json.loads(json.dumps(o))
            return output_dict


if __name__ == '__main__':
    API = API_reader(
        run=True,
        link='https://apiru.planfix.ru/xml',
        key1='key1fromplanfix',
        key2='key2fromplanfix',
        auth_xml_file='auth_and_get_sid-key.txt'
    )
    API.export_data(run=True, xml_file='get_tasks.txt', page=1)
    API.export_data(run=False, xml_file='get_projects.txt', page=1)

    create_csv = Parser(out_csv_file='full_csv.csv')
