"""
Вывести сумму последовательности чисел в строке
"""


def seq_sum(seq):
    try:
        lst = list(map(int, seq.split()))
    except ValueError:
        return "В последовательности должны быть только числа"
    if len(lst) == 0:
        return 0
    else:
        seq_sum = lst[0]
        for i in range(1,len(lst)):
            seq_sum += lst[i]
        return seq_sum

if __name__ == '__main__':
    print(seq_sum('a 2 3'))
    print(seq_sum('1 2 3'))
    print(seq_sum(''))
