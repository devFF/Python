from typing import Literal, Optional, Union
import datetime as dt
import requests
        
DATE_FORMAT = '%d.%m.%Y'

def cb_rf_currency_parser() -> dict:
    """Вытаскиваем актуальные значения курса из ЦБ РФ"""
    try:
        data = requests.get('https://www.cbr-xml-daily.ru/daily_json.js').json()
        rub_rate = 1
        usd_rate = float(data['Valute']['USD']['Value'])
        euro_rate = float(data['Valute']['EUR']['Value'])
    except:
        rub_rate, usd_rate, euro_rate = 1, 83.62, 90.28
    
    currency_dct = {
        'rub': {
            'rate': rub_rate,
            'currency_name': 'руб'
        },
        'usd': {
            'rate': usd_rate,
            'currency_name': 'USD'
        },
        'usd': {
            'rate': euro_rate,
            'currency_name': 'Euro'
        }
    }

    return currency_dct


class Record:
    """Класс для хранения данных"""
    def __init__(self, amount:int, comment:str, date:Optional[str] = None) -> None:
        self.amount = amount
        self.comment = comment
        if date is None:
            self.date = now = dt.datetime.now().date()
        else:
            self.date = dt.datetime.strptime(date, DATE_FORMAT).date()
    def __str__(self):
        return f"Количество: {self.amount}, комментарий: {self.comment}, дата: {self.date}"

class Calculator:
    """Родительский класс калькулятора с общими методами"""
    def __init__(self, limit) -> None:
        self.records = list()  # Создадим список для хранения записей.
        self.limit = limit

    def add_record(self, record: Record) -> None:
        """Метод сохранения записи"""
        self.records.append(record)
    
    def get_today_stats(self) -> Union[int, float]:
        """Итерируемся по экземплярам класса (записям) и если есть совпадения в дате, то суммируем amount"""
        return sum(
            record.amount for record in self.records if record.date == dt.date.today())

    def get_week_stats(self) -> Union[int, float]:
        """Итерируемся по экземплярам класса (записям) и если дата записи попадает в интервал прошедних 7 дней, то суммируем amount"""
        today = dt.date.today()
        last_week = today - dt.timedelta(days=7)
        return sum(
            record.amount for record in self.records if last_week <= record.date <= today)
    
    def get_limit_today(self) -> Union[int, float]:
        """Метод для вывода остатка денег/калорий"""
        return self.limit - self.get_today_stats()

class CaloriesCalculator(Calculator):
    """Дочерний класс калькулятора - калькулятор калорий"""
    def __init__(self, limit) -> None:
        super().__init__(limit)

    def get_calories_remained(self):
        limit =self.get_limit_today()
        if limit > 0:
            return f"Сегодня можно съесть что-нибудь ещё, но с общей калорийностью не более {limit} кКал"
        return "Хватит есть!"

class CashCalculator(Calculator):
    """Дочерний класс калькулятора - калькулятор денег"""
    def __init__(self, limit) -> None:
        super().__init__(limit)

    CURRENCY = Literal['rub', 'usd', 'eur']  # Определим возможые значения валюты
    ROUND_CALC = 2  # Округление до сотых

    def get_today_cash_remained(self, currency:CURRENCY) -> str:
         # Сделаем парсинг текущего курса валют от ЦБ РФ:
        currency_dct = cb_rf_currency_parser()

        value = round((self.get_limit_today()/currency_dct[currency]['rate']), self.ROUND_CALC)  # Перевод из рубля в заданную валюту
        currency_name = currency_dct[currency]['currency_name'] 
        if value > 0:
            return f"На сегодня осталось {value} {currency_name}"
        elif value == 0:
            return "Денег нет, держись"
        return f"Денег нет, держись: твой долг - {value} {currency_name}"


if __name__ == "__main__":
    limit = 1000
    cash_calculator = CashCalculator(limit)
    calories_calculator = CaloriesCalculator(limit)

    # Создаем записи - просто создаем экземпляры класса и записываем значения в его свойства
    # записи для денег 
    r1 = Record(amount=145, comment='кофе')
    r2 = Record(amount=300, comment='Серёге за обед')
    r3 = Record(amount=3000, comment='Бар на Танин день рождения', date='08.11.2022')

    # записи для калорий
    r4 = Record(amount=118, comment='Кусок тортика. И ещё один.')
    r5 = Record(amount=84, comment='Йогурт.')
    r6 = Record(amount=1140, comment='Баночка чипсов.', date='24.02.2019')

    # Записываем экземпляры класса в списки калькуляторов
    cash_calculator.add_record(r1)
    cash_calculator.add_record(r2)
    cash_calculator.add_record(r3)

    calories_calculator.add_record(r4)
    calories_calculator.add_record(r5)
    calories_calculator.add_record(r6)

    # вывод результатов
    print(cash_calculator.get_today_cash_remained('rub'))
    print(calories_calculator.get_calories_remained())
