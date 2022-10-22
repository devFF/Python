"""
Дан список из N слов (кортеж), длина каждого не превосходит K.
В записи каждого из M слов текста (каждое длиной до К)
может быть пропущена одна буква.
Для каждого слова сказать, входит ли оно (возможно с одной пропущенной буквой) в словарь (кортеж).
Решение:
В цикле по словам в словаре:
Для каждого слова сгенерировать множество различных слов с одной пропущенной буквой
Проверить вхождение word в это множество.
Так, для слова abcd множество будет состоять из: abcd, bcd, acd, acb
"""


def check_dict(dct, test_word):
    temp_list = set()
    for word in dct:
        temp_list.add(word)
        for i in range(len(word)):
            temp_list.add(word[:i] + word[i + 1:])
        # print(temp_list)
        if test_word in temp_list:
            return True
        temp_list = set()
    return None


if __name__ == '__main__':
    dct = ('my', 'preparing', 'to', 'exam')
    print(check_dict(dct=dct, test_word='exam'))
