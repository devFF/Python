import json
import re
import sys
import requests as r

"""
Работа программы:
1) Получаем IP адрес от PRTG
2) ПО IP получаем html-страницу веб-интерфейса принтера
3) Производим первичный парсинг и тестовые запросы к странице - пытаемся понять по какому шаблону парсить
4) Переходим на нужную страницу в веб-интерфейсе и парсим ее
5) Полученные данные выдаем PRTG: количество страниц, уровень тонера,
"""


def toner_level(toner_link, pattern):
    try:
        html_page = r.get(toner_link, verify=False, timeout=3)
    except:
        return None
    status = html_page.status_code
    if not status:
        return None
    text = html_page.text
    try:
        toner_level_str = re.findall(pattern, text)[0]
    except:
        return None
    if toner_level_str == '':
        return None
    try:
        toner_level = int(toner_level_str.replace('%', ''))
    except ValueError:
        return None
    return toner_level


def create_dict(ip):
    main_dict = {
        'P1':
            {
                'toner_link': f'http://{ip}',
                'printed_pages_link': None,
                'pattern': '<td style="WIDTH:(.*); MARGIN: 0px; HEIGHT:11px; BACKGROUND-COLOR: #000000',
                'desc': 'HP LaserJet Professional P1606dn старый интерфейс HP'
            },
        'P2':
            {
                'toner_link': f'http://{ip}/start/start.htm',
                'printed_pages_link': f'{ip}/start/StatCntFunc.htm',
                'pattern': 'TLevel\[0\] = (.*);\t//Jerald\tFunction name change\r',
                'desc': 'старый интерфейс KYOCERA FS-1128MFP'
            },
        'P3':
            {
                'toner_link': f'http://{ip}/startwlm/Hme_Toner.htm',
                'printed_pages_link': f'http://{ip}/dvcinfo/dvccounter/DvcInfo_Counter_PrnCounter.htm',
                'pattern': 'Renaming\[0\] = (.*) \+ "%";',
                'desc': 'новый интерфейс KYOCERA P2135dn'
            },
        'P4':
            {
                'toner_link': f'http://{ip}/status/GeneralStatus.html',
                'printed_pages_link': f'http://{ip}/status/GeneralStatus.html',
                'pattern': None,
                'desc': 'WorkCentre® 3550, пустой тонер (Empty), TODO!'
            },
        'P5':
            {
                'toner_link': f'http://{ip}/start/start.htm',
                'printed_pages_link': f'http://{ip}/start/StatCounter.html',
                'pattern': 'TColor\[TColorCnt\] = "Black"; TLevel\[TColorCnt\] = (.*);',
                'desc': 'старый интерфейс KYOCERA TASKalfa 181'
            },
        'P6':
            {
                'toner_link': f'http://{ip}/DevMgmt/ConsumableConfigDyn.xml',
                'printed_pages_link': f'http://{ip}/DevMgmt/ProductUsageDyn.xml',
                'pattern': '<dd:ConsumablePercentageLevelRemaining>(.*)</dd:ConsumablePercentageLevelRemaining>',
                'desc': 'http://hp04f66d.at.urfu.ru/#hId-pgConsumables - новый HP, вся инфа тут'
            },
        'P7':
            {
                'toner_link': f'http://{ip}/info_deviceStatus.html?tab=Home&menu=DevStatus',
                'printed_pages_link': f'http://{ip}/info_suppliesStatus.html?tab=Home&menu=SupplyStatus',
                'pattern': '''                     <td class="alignRight valignTop">
                       
                         
                           
                             (.*)%''',
                'desc': 'Цветной HP - убогий для парсинга, паттерн работает, но лучше переделать',
                'model': 'HP Color LaserJet MFP M477fdw'
            },
        'P8':
            {
                'toner_link': f'http://{ip}/general/status.html',
                'printed_pages_link': f'http://{ip}/general/information.html?kind=item',
                'pattern': '/common/images/black\.gif" alt="Black" class="tonerremain" height="(.*)" /',
                'desc': 'Уровень тонера по вертикальному размеру картинки',
                'model': 'Brother MFC-L2700DN series'
            },
        'P9':
            {
                'toner_link': f'http://{ip}/js/jssrc/model/startwlm/Hme_Toner.model.htm',
                'printed_pages_link': f'http://{ip}/js/jssrc/model/dvcinfo/dvccounter/DvcInfo_Counter_PrnCounter.model.htm',
                'pattern': "pp.Renaming\.push\(parseInt\('(.*)',",
                'desc': 'Новый интерфейс Kyocera принтеров из серии M2, какие-то проблемы с количеством страниц TODO',
                'model': 'ECOSYS M2540dn',
                'ip_example': '10.104.96.34'
            }
    }
    return main_dict


if __name__ == '__main__':
    # ОБРАБОТКА ВХОДНЫХ ДАННЫХ - принимаем IP принтера
    dct_from_server = json.loads(sys.argv[1])
    ip = dct_from_server['host']

    # ФОРМИРУЕМ СЛОВАРЬ С ШАБЛОНАМИ ДЛЯ ПАРСИНГА
    device_dict = create_dict(ip)

    # ПО ИЗВЕСТНЫМ ШАБЛОНАМ ПАРСИМ web-интерфейс принтера
    result = None
    for device in device_dict:
        toner_link = device_dict[device]['toner_link']
        pattern = device_dict[device]['pattern']
        result = toner_level(toner_link, pattern)
        if result is not None:
            break
    if result is None:
        result = 0

    # ФОРМИРОВАНИЕ СЛОВАРЯ
    output_dict = {
        "prtg": {
            "result": [
                {
                    "channel": "Toner level",
                    "value": result,
                    "unit": "Custom",
                    'LimitMinError': '1'
                },
            ],
            "text": 'Use message for debug'
        }
    }

    # ВЫВОД JSON для PRTG NETWORK MONITOR
    print(json.dumps(output_dict))
