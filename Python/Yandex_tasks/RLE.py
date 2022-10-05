"""
Дана строка, состоящая из букв A-Z:
AAAABBBCCXYZDDDDEEEFFFAAAAAABBBBBBBBBBBBBBBBBBBBBBBBBBBB
Нужно написать функцию RLE, которая на выходе даст строку вида:
A4B3C2XYZD4E3F3A6B28
Если символ встречается 1 раз, он остается без изменений, если символ повторяется более одного раза, к нему добавляется
количество повторений
Проверить строку на валидность
"""


def RLE(s):
    def compress(last_char, counter):
        if counter > 1:
            return last_char + str(counter)
        else:
            return last_char

    if len(s) > 0 and s.isalpha():
        last_char = s[0]
        counter = 1
        ans = []
        for i in range(1, len(s)):
            if s[i] != last_char:
                ans.append(compress(last_char, counter))
                last_char = s[i]
                counter = 0
            counter += 1
        ans.append(compress(last_char, counter))
        return "".join(ans)
if __name__ == '__main__':
    print(RLE('AAAABBBCCXYZDDDDEEEFFFAAAAAABBBBBBBBBBBBBBBBBBBBBBBBBBBB'))
