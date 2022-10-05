"""
Дана последовательность целых чисел длинной N (N>1)
Найти минимальное четное число в последовательности или вывести -1, если такого не существует
"""


def find_min_even(seq):
    ans = -1
    for i in range(len(seq)):
        if seq[i] % 2 == 0 and (ans == -1 or seq[i] < ans):
            ans = seq[i]
    return ans


if __name__ == '__main__':
    print(find_min_even((-1, -2, 2, 3, 4)))
    print(find_min_even((-1, -4, -2, 2, 3, 4)))
    print(find_min_even((-1, -2, -4, 3, 4)))
