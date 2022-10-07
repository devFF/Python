"""
Дана отсортированная последовательность чисел длиной N и число K.
Найти количество пар чисел A, B, таких что B - A > K
"""


def task(seq, k):
    j_start = 1
    ans = 0
    for i in range(len(seq)):
        for j in range(j_start, len(seq)):
            if seq[j] - seq[i] > k:
                j_start = j
                ans += len(seq) - j
                break
    return ans


if __name__ == '__main__':
    print(task(seq=[1, 3, 4, 6, 7, 11], k=4))
