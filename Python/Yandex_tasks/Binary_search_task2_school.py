"""
В управляющий совет школы входят родители, учителя и учащиеся школы, причем родителей должно быть не меньше одной трети
от общего числа членов совета. В настоящий момент времени в совет входит N человек, из них K родителей.
Определите сколько родителей нужно дополнительно ввести в совет, чтобы их число стало составлять не менее трети от числа
членов совета.
То есть K/M >= 1/3
или 3*K >= M
"""


def calc_num_of_parents(n, k):
    def check(n, k, m):
        return 3 * (k + m) >= n + m
    left = 0
    counter = 0
    right = n
    while left < right:
        m = (left + right) // 2
        if check(n,k,m):
            right = m - 1
        else:
            left = m + 1
        counter += 1
        print('step = {}, m = {}, left = {}, right = {}'.format(counter, m, left, right))
    if left > right:
        return 'Not found'
    else:
        return m


if __name__ == '__main__':
    print(calc_num_of_parents(n=100, k=3))
