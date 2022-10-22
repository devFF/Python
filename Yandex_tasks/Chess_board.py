"""
На шахматной доске NxN находятся M ладей (ладья бьет клетки на той же горизонтали
или вертикали до ближайшей занятой).
Определите, сколько пар ладей бьют друг друга. Ладьи задаются парой чисел
i и j, обозначающих координаты чисел.
1 <= N <= 10**9, 0 <= M <= 10**5
Решение:
Сделаем подсчет координат ладей по горизонтали и вертикали, так, в худшем случае
будет выполнено 2 * 10**5 итераций.
"""


def task(coords):
    dct_x, dct_y = {}, {}
    for i, j in coords:
        if i not in dct_x:
            dct_x[i] = 0
        if j not in dct_y:
            dct_y[j] = 0
        dct_x[i] += 1
        dct_y[j] += 1

    def count_pairs(dct):
        pairs = 0
        for key in dct:
            pairs += dct[key] - 1  # количество пар по прямой равно количество ладей N - 1
        return pairs

    return count_pairs(dct_x) + count_pairs(dct_y)


if __name__ == '__main__':
    coords = [(1, 10), (2, 10), (3, 10), (2, 9)]
    print(task(coords))
