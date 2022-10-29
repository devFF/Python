"""
Дан массив из нулей и единиц. Нужно определить, какой максимальный по длине подинтервал единиц можно получить,
удалив ровно один элемент массива.
Не проходит третий тест - доделать!
"""


def subinterval_max_len(seq):
    max_len = 0
    current_len = 1
    flag = True  # Еще не встречался элемент с другим значением
    last_val = seq[0]
    for i in range(1,len(seq)-1):
        #print('i = {}, value = {}, last_val = {}, counter = {}'.format(i, seq[i], last_val, current_len))
        if seq[i] == last_val:
            current_len += 1
        elif seq[i] != last_val and flag:
            flag = False
            continue
        elif seq[i] != last_val and not flag:
            flag = True
            max_len = current_len if current_len > max_len else max_len
            last_val = seq[i]
            current_len = 1
    # обработка последнего элемента
    if seq[-1] == last_val:
        current_len += 1
        max_len = current_len if current_len > max_len else max_len
    else:
        max_len = current_len if current_len > max_len else max_len
    return max_len

print(subinterval_max_len(seq=[1, 1, 0]))  # ANS: 2
print(subinterval_max_len(seq=[0, 1, 0]))  # ANS: 2
print(subinterval_max_len(seq=[0, 1, 1]))  # ANS: 2
print(subinterval_max_len(seq=[1, 1, 0, 1, 1, 0, 0, 0]))  # ANS: 4
print(subinterval_max_len(seq=[1, 1, 0, 1, 1, 0, 0, 0, 0, 0]))  # ANS: 5
print(subinterval_max_len(seq=[1, 1, 0, 1, 1, 0, 0, 0, 0, 0, 1]))  # ANS: 5
