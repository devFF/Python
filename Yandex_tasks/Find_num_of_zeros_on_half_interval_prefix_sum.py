"""
Дана последовательность чисел длиной N и M запросов
Запросы: Сколько нулей на полуинтервале [L,R)
[0,1,2,3,0,0,0,4,0,3,2,0,1,0,0]
Ans: 8
Решение, создадим префиксную сумму, считающую нули. Тогда достаточно один раз посчитать ее и затем выводить разность
prefix_sum[R]-prefixsum[L], чтобы определить количество нулей на полуинтервале [L,R)
"""


def prefix_zeroes_sum(seq):
    pref_sum = [0]
    for i in range(1, len(seq) + 1):
        if seq[i - 1] == 0:
            pref_sum.append(pref_sum[i - 1] + 1)
        else:
            pref_sum.append(pref_sum[i - 1])
    return pref_sum


class FindNumberZeroes:
    def __init__(self, seq):
        self.prefix_sum = prefix_zeroes_sum(seq)

    def number_zeroes(self, L, R):
        return self.prefix_sum[R] - self.prefix_sum[L]


if __name__ == '__main__':
    obj = FindNumberZeroes(seq=[0, 1, 2, 3, 0, 0, 0, 4, 0, 3, 2, 0, 1, 0, 0])
    print(obj.number_zeroes(L=0, R=6))
    print(obj.number_zeroes(L=0, R=2))
    print(obj.number_zeroes(L=0, R=15))
