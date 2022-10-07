"""
Пример реализации бинарного поиска
"""


def bin_search(seq, val):
    l = 0
    r = len(seq)
    m = (l + r) // 2
    counter = 0
    while seq[m] != val and l <= r:
        if seq[m] > val:
            r = m - 1
        else:
            l = m + 1
        m = (r + l) // 2
        counter += 1
    if l > r:
        return 'No such number, {} iterations'.format(counter)
    else:
        return 'Found {} in pos {} with {} iterations'.format(seq[m], m, counter)


if __name__ == '__main__':
    seq = [i for i in range(0, 1_000_000, 2)]
    print(bin_search(seq, 800))
    print(bin_search(seq, 799))
    print(bin_search(seq, 650_000))
