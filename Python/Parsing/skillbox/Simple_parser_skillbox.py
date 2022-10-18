from bs4 import BeautifulSoup
import requests

def first_parser():
    html_file = open('skillbox.html', 'r', encoding='utf-8')
    html_code = html_file.read()
    soup = BeautifulSoup(html_code, 'html.parser')

    # Найти заголовки всех ссылок
    # string - вернуть строкове представление, strip - удалить пробельные символы
    links = soup.find_all('a')
    link_titles = [link.string.strip() for link in links]

    # обращение по атрибутам, ex: выведем ссылки
    # href - атрибут
    link_list = [link['href'] for link in links]
    print(link_list)


def second_parser():
    html_code = requests.get('https://live.skillbox.ru/').content  # get-запрос, получение html-кода страницы
    soup = BeautifulSoup(html_code, 'html.parser')
    # Найдем заголовки вебинаров по классу, к которому они относятся, см html-код:
    webinars = soup.find_all(class_ = 'webinar-card__title')
    webinars_list = [webinar.string.strip() for webinar in webinars]

    # Также для даты
    webinars = soup.find_all(class_='webinar-card__date')
    webinars_list = [webinar.string.strip() for webinar in webinars]

    # Но это не совсем удобно, разумно для каждого вебинара найти более общий класс и в нем искать нужные подклассы
    items = soup.find_all(class_='webinar-card__info')
    for webinar in items:
        title = webinar.find(class_ = 'webinar-card__title').string.strip()
        date = webinar.find(class_ ='webinar-card__date').string.strip()
        print(f'Вебинар {title} прошел {date}')


second_parser()
