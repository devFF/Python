# Интенсив от skillbox по парсингу сайтов
В целом, реализованы довольно простые задачи, но на основе этих проектов можно реализовать довольно сложные проекту по парсингу сайтов. 
Данные скрипты могут быть использованы как шпаргалка для создания скриптов для парсинга.

- [Simple_parser_skillbox.py](https://github.com/devFF/FindJob/blob/main/Parsing/skillbox/Simple_parser_skillbox.py) -
парсинг простой [html-страницы](https://github.com/devFF/FindJob/blob/main/Parsing/skillbox/skillbox.html). Парсинг страницы с вебинарами от skillbox библиотекой BeautifulSoup - получаем заголовок вебинара и дату его проведения.

- [parse_autoru_by_API.py](https://github.com/devFF/FindJob/blob/main/Parsing/skillbox/parse_autoru_by_API.py) - 
парсинг сайта auto.ru при помощи API (готовый шаблон для запроса), который может быть обнаружен при помощи web inspector в вкладке network Fetch/XHR. 
Вытаскиваем данные о пробеге и цене для выбранной модели. 
Недостаток данного метода заключается в том, что служебная информация для запроса может быть изменена в любой момент времени и скрипт перестанет работать.
Преимущество данного метода - в ответе от сервера получим json-файл, который без лишних библиотек может быть преобразован в словарь Python.

- [selenium_parser.py](https://github.com/devFF/FindJob/blob/main/Parsing/skillbox/selenium_parser.py) - 
парсинг сайта hh.ru с использованием библиотеки Selenium. Реализуется примитивная задача - узнать количество вакансий для заданной профессии. 
Важно, для корректной работы Selenium версия **chromedriver_binary** должна совпадать с версией браузера Google Chrome.

- [parser_telegram_bot](https://github.com/devFF/FindJob/tree/main/Parsing/skillbox/parser_telegram_bot) - 
в завершении интенсива был создан бот для телеграм, который выполняет функцию программы [selenium_parser.py](https://github.com/devFF/FindJob/blob/main/Parsing/skillbox/selenium_parser.py)

