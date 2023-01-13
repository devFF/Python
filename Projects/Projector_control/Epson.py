import json
import PySimpleGUI as sg
import socket
import re
import sys
import os
import getpass


def run_config():
    """Создание файла конфигурации и его чтение"""
    if os.path.exists(config_file):
        with open(config_file, 'r') as cfg:
            str_data = cfg.read()
        json_data = json.loads(str_data)
    else:
        json_data = {
            'ip': '10.104.1.193',
            'dns': 'K48-338-EPSON',
            'autorun_status': True,
            'PORT': 4352
        }
        str_data = json.dumps(json_data)
        with open(config_file, 'w') as cfg:
            cfg.write(str_data)
    return json_data


def edit_config():
    """Сохранение настроек программы в файл конфигурации"""
    if os.path.exists(config_file):
        with open(config_file, 'r') as cfg:
            str_data = cfg.read()
        json_data = json.loads(str_data)
    else:
        json_data = run_config()
    json_data['ip'] = values['_ip_']
    json_data['PORT'] = values['_PORT_']
    json_data['autorun_status'] = values['_autorun_']

    str_data = json.dumps(json_data)
    with open(config_file, 'w') as cfg:
        cfg.write(str_data)


def resource_path(relative_path):
    """Фикс бага, из-за которого некорректно отображаются иконки программы"""
    base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)


def switch_autorun(activate=True):
    """Реализация автозапуска программы при включении компьютера"""
    file_path = os.path.join(current_dir, 'Epson.exe')
    bat_path = r'C:\Users\%s\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup' % USER_NAME
    if activate:
        with open(bat_path + '\\' + "open.bat", "w+") as bat_file:
            bat_file.write(r'start "" %s' % file_path)
    else:
        try:
            os.remove(bat_path + "\open.bat")
        except FileNotFoundError:
            pass


def create_window():
    """Весь front-end"""
    sg.theme('LightBlue2')
    status, color = power_status()
    menu_tab = [
        [sg.Text('Статус проектора: '), sg.Text(text=status, key='_status_', text_color=color)],
        [sg.Button(button_text='Включить'), sg.Button(button_text='Выключить'), sg.Button(button_text='Статус')]
    ]

    settings_tab = [
        [sg.Text('IP проектора:'), sg.InputText(size=(14, 2), default_text=ip, key="_ip_")],
        [sg.Text('Порт:             '), sg.InputText(size=(14, 2), default_text=PORT, key="_PORT_")],
        [sg.Checkbox(text='Автозапуск', tooltip='Запускать программу при включении компьютера', default=autorun_status,
                     key='_autorun_'), sg.Button(button_text='Применить')]
    ]

    layout = [
        [sg.TabGroup([[sg.Tab('Меню', menu_tab), sg.Tab('Настройки', settings_tab)]]), ]
    ]
    window = sg.Window('Управление проектором', layout, icon=resource_path('icon.ico'), font=("Helvetica", 16))
    return window


def power_status():
    """Проверка статуса проектора"""
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.settimeout(3)
        try:
            s.connect((ip, PORT))
            s.recv(1024)
        except (TimeoutError, socket.gaierror):
            return 'Не доступен', 'red'

        s.sendall(b'%1POWR ?\r')
        data = str(s.recv(1024))
    if '1POWR' in data:
        data = re.sub(pattern='1POWR', repl='', string=data, count=0)
        try:
            status = int(re.sub(pattern='\D', repl='', string=data))
        except ValueError:
            return "Ошибка", "red"
        if status == 1:
            return "Включен", "green"
        elif status == 3:
            return "Разогрев", "green"
        else:
            return "Выключен", "red"


def switch_power(set):
    """Реализация включения/выключения проектора"""
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.settimeout(2)
        try:
            s.connect((ip, PORT))
            s.recv(1024)
        except (TimeoutError, socket.gaierror):
            return None

        if set == 'on':
            s.sendall(b'%1POWR 1\r')
        if set == 'off':
            s.sendall(b'%1POWR 0\r')
        s.recv(1024)


if __name__ == '__main__':
    USER_NAME = getpass.getuser()  # Имя пользователя, чтобы перейти в папку, где разрешено создание файлов
    current_dir = os.getcwd()  # Сохраняем директорию расположения исполняемого файла
    os.chdir(f'C:\\Users\\{USER_NAME}')  # Переходим в директорию, где разрешено создание файлов
    config_file = 'Epson_config.txt'
    config_data = run_config()  # Создаем/читаем файл конфигурации
    ip = config_data['ip']
    try:
        PORT = int(config_data['PORT'])
    except (ValueError, TypeError):
        PORT = 4352
    autorun_status = config_data['autorun_status']  # Узнаем статус проектора

    window = create_window()  # Создаем интерфейс программы
    while True:
        event, values = window.read()
        if event in (None, 'Exit', 'Cancel'):
            break
        if event == 'Включить':
            try:
                switch_power(set='on')
            except ValueError:
                pass
        if event == 'Выключить':
            try:
                switch_power(set='off')
            except ValueError:
                pass
        if event == 'Статус':
            status, color = power_status()
            window['_status_'].Update(status)
            window['_status_'].Update(text_color=color)
        if event == 'Применить':
            ip = values['_ip_']
            try:
                PORT = int(values['_PORT_'])
            except (ValueError, TypeError):
                PORT = 4352
            activate = values['_autorun_']
            edit_config()
            if values['_autorun_']:
                switch_autorun(activate=True)
            if not values['_autorun_']:
                switch_autorun(activate=False)
