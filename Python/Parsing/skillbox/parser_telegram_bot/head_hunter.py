from selenium import webdriver  # импорт движка
from selenium.webdriver.chrome.options import Options
import chromedriver_binary  # прослойка между кодом и браузером, установить версию == версии браузера
import time
from selenium.webdriver.common.by import By  # для поиска по CSS-селекторам
import re


def launch_parser(title):
    options = Options()
    options.headless = True
    browser = webdriver.Chrome(options=options)  # Запуск браузера
    browser.get('http://hh.ru')  # Открываем hh.ru

    # Найдем поле поискового запроса и введем текст
    # Данное поле точно характеризует id (см. веб-инспектор хрома), поэтому определяем поле по нему
    search_input = browser.find_element(By.ID, 'a11y-search-input')
    search_input.send_keys(title)  # Отправили текст в поле

    # Найдем кнопку поиска и нажмем на нее
    search_button = browser.find_element(By.CSS_SELECTOR, '[data-qa="search-button"]')
    search_button.click()

    # Найдем заголовок с количеством вакансий и выведем их количество
    """<div data-qa="vacancies-search-header">
    <div class="bloko-v-spacing bloko-v-spacing_base-6"></div>
    <h1 data-qa="bloko-header-3" class="bloko-header-section-3">
    7 
    <span>вакансий</span> 
    «Junior Python»
    </h1>
    <div class="bloko-v-spacing bloko-v-spacing_base-4"></div></div>
    """
    # исходя из структуры видно, что данные нужно получить по селектору по объявлению заголовка h1 - объявим чз пробел
    vacancy_number = browser.find_element(By.CSS_SELECTOR, '[data-qa="vacancies-search-header"] h1').text

    # Заменим все символы, не являющиеся цифрой
    count = re.sub(r'\D', '', vacancy_number)

    # print(f"Количество вакансий с запросом «Junior Python»: {count}")

    browser.close()

    return count
