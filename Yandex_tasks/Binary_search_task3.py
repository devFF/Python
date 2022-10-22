"""
Юра решил подготовиться к собеседованию в Яндекс. Он выбрал на сайте leetcode N задач. В первый день Юра решил K задач,
а в каждый следующий день Юра решал на одну задачу больше, чем в предыдущий день.
Определите, сколько дней уйдет у Юры на подготовку к собеседованию.
"""


def bin_search(n, k):
    def check(k,m):
        return (2*k+m-1)*m // 2 >= n
    left = 0
    right = n
    counter = 0
    while left <= right:
        m = (left + right) // 2
        if check(k,m):
            right = m - 1
        else:
            left = m + 1
        counter += 1
        print('step = {}, m = {}, check = {}, left = {}, right = {}'.format(counter, m, check(k,m), left, right))
    return m


if __name__ == '__main__':
    print(bin_search(10,1))