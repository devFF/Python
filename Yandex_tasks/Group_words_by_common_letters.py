"""
Сгруппировать слова по общим буквам
Sample Input: ["eat", "tea","tan","ate","nat","bat"]
Sample Output: [["eat", "tea","ate"],["tan","nat"],["bat"]]
Отсортировать буквы в каждом слове, для каждого нового слова создать ключ и в значение записывать количество одинаковых
"""


def group_words(words_list):
    dct = {}
    for word in words_list:
        sorted_word = ''.join(sorted(word))
        if sorted_word not in dct:
            dct[sorted_word] = []
        dct[sorted_word].append(word)
    ans = []
    for key in dct:
        ans.append(dct[key])
    return ans


if __name__ == '__main__':
    print(group_words(["eat", "tea", "tan", "ate", "nat", "bat"]))
