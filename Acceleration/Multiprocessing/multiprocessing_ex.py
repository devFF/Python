from multiprocessing import Pool
import time


def my_func(x):
    """Если число является простым, то выведем его"""
    if x <= 1:
        return 0
    elif x <= 3:
        return x
    elif x % 2 == 0 or x % 3 == 0:
        return 0
    i = 5
    while i ** 2 <= x:
        if x % i == 0 or x % (i + 2) == 0:
            return 0
        i += 6
    return x


if __name__ == '__main__':
    t0 = time.time()
    with Pool(4) as p:
        answer = sum(p.map(my_func, list(range(1_000_000))))
    print('Параллельное вычисление выполнено за {}, ответ: {}'.format(time.time() - t0, answer))

    t0 = time.time()
    answer = sum(map(my_func, range(1_000_000)))
    print('Последовательное вычисление выполнено за {}, ответ: {}'.format(time.time() - t0, answer))