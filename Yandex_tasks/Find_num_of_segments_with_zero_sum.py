"""
Дана последовательность чисел длиной N.
Необходимо найти количество отрезков с нулевой суммой.
Решение за N^2: смещаем указатель
Решение за N: использовать префиксную сумму -- доделать!
"""


def count_zeroes_segments(seq):
    ans = 0
    for i in range(len(seq)):
        range_sum = 0
        for j in range(i, len(seq)):
            range_sum += seq[j]
            if range_sum == 0:
                ans += 1
    return ans


if __name__ == '__main__':
    print(count_zeroes_segments([-1, 1, -1, 1]))
