def define_ranges(seq):
    if len(seq) == 0:
        return 'Невалидная последовательность'
    answer = []
    seq = sorted(seq)
    sub_start = seq[0]
    sub_end = seq[0]

    for i in range(1, len(seq)):
        print(seq[i])
        if seq[i] - seq[i - 1] == 1:
            sub_end = seq[i]
        elif seq[i] - seq[i - 1] != 1:
            if sub_start != sub_end:
                answer.append(f'{sub_start}-{sub_end}')
            else:
                answer.append(f'{sub_start}')
            sub_start = seq[i]
            sub_end = seq[i]

        if i == len(seq) - 1:
            if sub_start != sub_end:
                answer.append(f'{sub_start}-{sub_end}')
            else:
                answer.append(f'{sub_start}')
    return ','.join(answer)


print(define_ranges([1, 4, 6, 2, 3, 9, 8, 11, 12, 0, 14]))
