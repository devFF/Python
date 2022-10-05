"""
Дано два числа X и Y без ведущи нулей.
Необходимо проверить, можно ли получить первое из второго перестановкой цифр.
Решение простым подсчетом
"""


def check_numbers(x, y):
    def count_digits(num):
        digitcounter = [0] * 10  # 0 1 2 ... 9 -- все цифры = 10 штук
        while num > 0:
            last = num % 10
            digitcounter[last] += 1
            num = num // 10
        return digitcounter
    dict_x = count_digits(x)
    dict_y = count_digits(y)
    for i in range(10):
        if dict_x[i] != dict_y[i]:
            return False
    return True





if __name__ == '__main__':
    print(check_numbers(x=2021, y=1202))
    print(check_numbers(x=12021, y=1202))
