def bs(seq, val):
    l = 0
    r = len(seq)
    m = (l + r) // 2
    while val != seq[m] and l <= r:
        if val < seq[m]:
            r = m - 1
        else:
            l = m + 1
        m = (l + r) // 2
    if l > r:
        print('Not found')
    else:
        print('Found')


bs(seq=(0, 1, 2, 3, 5, 6, 7, 8, 9, 10), val=-1)
