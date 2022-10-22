"""
Даны две отсортированные последовательности чисел (длиной N и M соответственно).
Необходимо слить их в одну отсортированную последовательность.
"""

from heapq import merge


def simple_method(seq1, seq2):
    return list(merge(seq1, seq2))


def double_pointer(seq1, seq2):
    counter1, counter2 = 0, 0
    merged_list = []
    while counter1 < len(seq1) and counter2 < len(seq2):
        if seq1[counter1] <= seq2[counter2]:
            merged_list.append(seq1[counter1])
            counter1 += 1
        else:
            merged_list.append(seq2[counter2])
            counter2 += 1
    if len(seq1) > len(seq2):
        return merged_list + seq1[counter1:]
    else:
        return merged_list + seq2[counter2:]


if __name__ == '__main__':
    seq1 = [1, 3, 4, 6, 7, 11]
    seq2 = [1, 2, 3, 4, 5]
    print(simple_method(seq1, seq2))
    print(double_pointer(seq1, seq2))
    print(double_pointer(seq2, seq1))
