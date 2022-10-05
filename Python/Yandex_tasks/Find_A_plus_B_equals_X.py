"""
Дана последовательность положительных чисел длиной N и число X.
Нужно найти два различных числа A и B из последовательности, таких что A+B=X
или вернуть пару 0, 0, если такой пары чисел нет
"""


def find_ab(seq, x):
    checked_list = set()
    for num in seq:
        if x - num in checked_list:
            return num, x-num
        checked_list.add(num)
    return 0, 0


if __name__ == '__main__':
    print(find_ab(seq=(1, 2, 3, 4, 5, 6, 7, 8, 9), x=7))
