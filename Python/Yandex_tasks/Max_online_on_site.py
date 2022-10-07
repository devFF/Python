"""
Сайт посетило N человек, для каждого известно время входа на сайт In, и время выхода с сайта Out.
Считается, что человек был на сайте с момента In по Out включительно.
Определите, какое максимальное количество человек было на сайте одновременно
Решение методом сортировки событий.
"""


def define_max_online(time_in, time_out):
    person_in = -1  # Человек зашел, будем сортировать, поэтому значение меньше, чем person_out
    person_out = 1  # Человек вышел
    max_online = 0
    online = 0
    events = []
    for i in range(len(time_in)):
        events.append((time_in[i], person_in))  # используем person in/out для определения события дальше
        events.append((time_out[i], person_out))
    events = sorted(events)
    print(events)
    for event in events:
        if event[1] == -1:
            online += 1
        else:
            online -= 1
        max_online = max(online, max_online)
    return max_online


time_in = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
time_out = [3, 5, 6, 8, 8, 10, 12, 13, 14, 14]

print(define_max_online(time_in, time_out))
