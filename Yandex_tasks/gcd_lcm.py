"""
gcd - greatest common divisor (НОД - наибольший общий делитель)
lcm - least common multiple (НОК - наименьшее общее кратное)
НОД - Наибольшее число С, которое делит A и B без остатка
НОК - Наименьшее число C, на которое числа A и B делятся без остатка
1) Простейший способ найти НОД:
1. Найти наименьшее число среди A и B, так limit = min(A,B)
2. В цикле для i от limit до 1 (быстрее искать с конца) найдем такое число, что A % i == 0 and B % i == 0
3. Условие выполнилось, нашли НОД
2) Простейший способ найти НОК:
1. Найти наибольшее число max(A,B) = start
2. В цикле while прибавляем счетчику i(который изначально равен start) единицу до тех пор, пока не выполнится условие
C % A == 0 и C % B == 0
3. return i при выполнении условия (выход из цикла while)

TODO: Разобрать более быстрые алгоритмы определения НОК и НОД!
"""


def my_gcd_v1(A, B):
    limit = min(A, B)
    for i in range(limit, 1, -1):
        if A % i == 0 and B % i == 0:
            return i


def my_lcm_v1(A, B):
    counter = max(A, B)
    while True:
        if counter % A == 0 and counter % B == 0:
            return counter
        counter += 1


print(my_gcd_v1(A=10, B=20))
print(my_gcd_v1(A=8, B=20))
print(my_lcm_v1(A=10, B=20))
print(my_lcm_v1(A=8, B=20))
