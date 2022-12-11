import numpy as np
import requests
import json
import pandas as pd

pd.set_option('display.max_columns', None)


def get_devices_from_base(host: str, login: str, password: str, printer_group_id: int = None,
                          camera_group_id: int = None, projector_group_id: int = None, router_group_id: int = None):
    """
    Функция получает список сетевых устройств, которые уже добавлены в систему PRTG network monitor. \n
    :param host: ip сервера, на котором запущена система мониторинга
    :param login: логин администратора
    :param password: пароль администратора
    :param printer_group_id: номер группы принтеров
    :param camera_group_id: номер группы камер
    :param projector_group_id: номер группы проекторов
    :param router_group_id: номер группы роутеров
    :return: None
    """
    group_list = [printer_group_id, camera_group_id, projector_group_id, router_group_id]
    df_common = None
    for group_id in group_list:
        if group_id is not None:
            data = requests.get(
                f'http://{host}/api/table.json?content=devices&columns=device,host,group&id={str(group_id)}&username={login}&password={password}')
            data_string = data.text
            data_dict = json.loads(data_string)
            devices = data_dict['devices']
            df_devices = pd.DataFrame.from_records(devices)
            df_devices = df_devices.rename(columns={'device': 'name_', 'host': 'ip_', 'group': 'type'})
            if df_common is None:
                df_common = df_devices
            else:
                df_common = pd.concat([df_common, df_devices], sort=False)
    if df_common is not None:
        df_common.to_csv('devices_in_base.csv', index=False, sep=';')


def find_network_protocol_devices(open_csv, save_csv):
    """
    Метод сохраняет csv-файл с устройствами, имеющие один из сетевых протоколов http, https, ftp. \n
    :param save_csv: Название файла с указанием расширения csv
    :param open_csv: Данный файл получен в результате экспорта сканирования всей сети в advanced ip scanner
    :return: None
    """
    df = pd.read_csv(open_csv, on_bad_lines='skip', encoding="utf-16", sep='\t')
    df = df[['Имя', 'IP', 'Http', 'Https', 'Ftp']]  # Много лишних колонок, избавимся от них, указав нужные
    df = df.rename(columns={'Имя': 'name', 'IP': 'ip', 'Http': 'http', 'Https': 'https', 'Ftp': 'ftp'})
    # Если все протоколы пустые, то удаляем их таблицы (оставляем те, где хоть один не nan):
    df = df.fillna('Unknown')
    df = df[(df['http'] != 'Unknown') | (df['https'] != 'Unknown') | (df['ftp'] != 'Unknown')]
    df.to_csv(save_csv, index=False, sep=';')  # Сохраняем файл с устройствами, имеющие сетевой протокол


def device_classificator(df_merged):
    key_words_dict = {
        'printer': ['hp', 'xerox', 'laserjet', 'kyocera', 'ecosys', 'color', 'pantum', 'print', 'p01',
                    'p02', 'p03', 'kyo', 'bm5100adn', 'xrx'],
        'projector': ['epson', 'panasonic', 'nec', 'projector'],
        'router': ['router', 'tp-link', 'switch', 'cisco'],
        'camera': ['hikvision', 'prestel', 'camera']
    }
    name_list = df_merged['name'].to_list()
    http_list = df_merged['http'].to_list()
    ftp_list = df_merged['ftp'].to_list()
    type_list = []
    for name, http, ftp in zip(name_list, http_list, ftp_list):
        flag = True
        for category in key_words_dict:
            for word in key_words_dict[category]:
                if flag and (word in name.lower() or word in http.lower() or word in ftp.lower()):
                    type_list.append(category)
                    flag = False
                    break
        if flag:
            type_list.append('Unknown')

    df_merged['type'] = type_list
    return df_merged


def select_new_devices(devices_in_base_csv, new_devices_csv):
    """
    Метод создает csv-файл с данными о сетевых устройствах, которых еще нет в базе PRTG. \n
    :param devices_in_base_csv: название csv-файла с устройствами, которые уже есть в базе PRTG мониторинга.
    :param new_devices_csv: название csv-файла с устройствами имеющих с сетевой протокол, которые были
    найдены при последнем сканировании сети.
    :return: None
    """

    df_devices_in_base = pd.read_csv(devices_in_base_csv, encoding='utf-8', sep=';')
    df_new_devices = pd.read_csv(new_devices_csv, encoding='utf-8', sep=';')
    # Объединим таблицы по ip
    df_merged = df_devices_in_base.merge(df_new_devices, left_on='ip_', right_on='ip', how='outer')
    df_merged = df_merged.fillna('Unknown')
    # Оставим только новые устройства, у которых ip_ (ip известного устройства) != ip (нового устройства)
    df_merged = df_merged[(df_merged['ip_'] != df_merged['ip']) & (df_merged['name_'] == 'Unknown')]
    # Уберем лишние колонки, которые использовались для фильтрации в предыдущем шаге (выделим нужные)
    df_merged = df_merged[['name', 'ip', 'http', 'https', 'ftp', 'type']]

    # Классификация устройств
    df_merged = device_classificator(df_merged)

    # Сохранение таблицы с новыми устройствами
    df_merged.to_csv('new_devices.csv', sep=';')

    # Статистика
    print('Total found {}:'.format(len(df_merged['type'])))
    print(df_merged['type'].value_counts())


if __name__ == '__main__':
    get_devices_from_base(host='your_ip', login='your_login', password='your_password',
                          printer_group_id=56,
                          camera_group_id=2171,
                          projector_group_id=2249,
                          router_group_id=53)
    find_network_protocol_devices(open_csv='all_found_devices.csv',
                                  save_csv='all_found_network_protocol_devices.csv')
    select_new_devices(devices_in_base_csv='devices_in_base.csv',
                       new_devices_csv='all_found_network_protocol_devices.csv')
