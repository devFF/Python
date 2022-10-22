"""
Найти максимальное значение в последовательности
"""


def seq_max(seq):
    if len(seq) == 0:
        return 0
    else:
        try:
            seq = list(map(int, seq.split()))
        except ValueError:
            return "В последовательности должны быть только числа"
        max_val = seq[0]
        for i in range(1, len(seq)):
            if seq[i] > max_val:
                max_val = seq[i]
        return max_val


if __name__ == '__main__':
    print(seq_max('1 1 1'))
    print(seq_max('a 1 1'))
    print(seq_max('1 2 3'))
    print(seq_max('3 2 1'))
    print(seq_max('-1 1 -2'))
    print(seq_max('1'))
