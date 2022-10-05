"""
Дана строка в кодировке UTF-8
Найти самый часто встречающийся в ней символ.
Если несколько символов встречаются одинаково часто, то можно вывести любой
Сложность O(N+K)
N - количество символов
K - количество разновидностей символов
"""


def find_char(some_str):
    if len(some_str) != 0:
        dct = {}
        for i in range(len(some_str)):
            if some_str[i] not in dct:
                dct[some_str[i]] = 0
            dct[some_str[i]] += 1
        count = 0
        for key in dct:
            if dct[key] > count:
                ans = key
                count = dct[key]
        return ans


if __name__ == '__main__':
    print(find_char('a'))
    print(find_char(''))
    print(find_char('aaaaabbc'))
    print(find_char('aaaaabbbbbbbc'))