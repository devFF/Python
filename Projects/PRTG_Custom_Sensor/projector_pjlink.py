import json
import socket
import re
import sys


dct_from_server = json.loads(sys.argv[1])
host = dct_from_server['host']
port = 4352


def answer_processing(data):
    data = str(data)
    if '1POWR' in data:
        data = re.sub(pattern='1POWR', repl='', string=data, count=0)
        status = int(re.sub(pattern='\D', repl='', string=data))
        if status == 1:
            return 1, "POWER ON"
        else:
            return 0, "STANDBY"

    if '%1LAMP' in data:
        data = re.sub(pattern='%1LAMP', repl='', string=data, count=0)
        data_list = data.split()
        status = re.sub(pattern='\D', repl='', string=data_list[0])
        return status

    if '%1INPT' in data:
        port_dict = {
            31: 'HDMI1',
            32: 'HDMI2',
            33: 'Diplay port',
            34: 'HDBaseT',
            35: 'SDI'
        }
        data = re.sub(pattern='%1INPT', repl='', string=data, count=0)
        port_number = int(re.sub(pattern='\D', repl='', string=data))
        if port_number in port_dict:
            return port_dict[port_number]
        else:
            return 'Unidentified port'


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    # ПОДКЛЮЧЕНИЕ
    s.connect((host, port))
    conn_message = (s.recv(1024))

    # ЗАПРОС СТАТУСА
    s.sendall(b'%1POWR ?\r')
    power_status, power_status_text = answer_processing(s.recv(1024))
    message = 'Status: {}, '.format(power_status_text)

    # ЗАПРОС ВРЕМЕНИ РАБОТЫ ЛАМПЫ
    s.sendall(b'%1LAMP ?\r')
    lamp_time = answer_processing(s.recv(1024))

    # ЗАПРОС ПОДКЛЮЧЕННЫХ ПОРТОВ
    s.sendall(b'%1INPT ?\r')
    input_port = answer_processing(s.recv(1024))
    message += 'Input port: {}'.format(input_port)

    # Вывод параметра в сообщение для отладки
    #message += ', {}'.format(test_param)


# ФОРМИРОВАНИЕ СЛОВАРЯ
output_dict = {
    "prtg":{
        "result": [
        {
            "channel": "Power status",
            "value": power_status,
            "unit": "Custom"
        },
        {
            "channel": "Lamp time",
            "value": lamp_time,
            "unit": 'TimeHours'
        }
        ],
        "text": message
    }
}

# ВЫВОД JSON для PRTG NETWORK MONITOR
print(json.dumps(output_dict))
