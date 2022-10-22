"""
Дана последовательность слов.
Вывести все самые короткие слова через пробел.
Решить в два прохода.
Сначала найти самую короткую длину,
затем по соответствию этой длине найти слова
"""


def sortest_words(seq):
    min_len = len(seq[0])
    for i in range(1, len(seq)):
        if len(seq[i]) < min_len:
            min_len = len(seq[i])
    words_list = []
    for i in range(len(seq)):
        if len(seq[i]) == min_len:
            words_list.append(seq[i])
    return " ".join(words_list)


if __name__ == '__main__':
    print(sortest_words(seq=('aa', 'bbb', 'cc', 'dddd')))
