"""
Дана последовательность целых чисел длиной N
Найти первое (левое) вхождение положительного числа Х в нее или вывести -1, если число Х не встречалось
"""


def find_last_x_pos(seq, x):
    try:
        x = int(x)
    except ValueError:
        return 'Введите целое число'
    if len(seq) == 0:
        return '-1'
    else:
        try:
            seq = list(map(int, seq.split()))
        except ValueError:
            return '-1'
        ans = -1
        for i in range(len(seq)-1, 0, -1):
            if seq[i] == x and ans == -1:  # или удалить условие "and ans == -1"
                ans = i
        return ans


if __name__ == '__main__':
    print(find_last_x_pos(seq='-1 -4 2 4 0', x='a'))
    print(find_last_x_pos(seq='-1 -4 3 2 4 0 1', x='2'))
    print(find_last_x_pos(seq='-1 -4 -2 4 0', x='2'))
    print(find_last_x_pos(seq='', x='2'))
