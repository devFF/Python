"""
Дана строка S.
Выведите гистограмму как в примере (коды символов отсортированы).
S = Hello, world!
Вывод программы:
      #
      ##
##########
 !,Hdelorw
Решение:
Итерация по строке, на каждой итерации проверяем вхождение символа(ключа) в словарь и добавляем в значение единицу.
Также отслеживаем максимальную высоту.
Сортируем список ключей.
"""


def string_to_histogram(s):
    dct = {}
    max_h = 0
    for sym in s:
        if sym not in dct:
            dct[sym] = 0
        dct[sym] += 1
        if dct[sym] > max_h:
            max_h = dct[sym]
    sorted_keys = sorted(list(dct.keys()))
    for now_h in range(max_h, 0, -1):
        str_to_print = ''
        for key in sorted_keys:
            if dct[key] < now_h:
                str_to_print += ' '
            else:
                str_to_print += '#'
        print(str_to_print)
    print(''.join(sorted_keys))


if __name__ == '__main__':
    string_to_histogram('Hello, world!')
