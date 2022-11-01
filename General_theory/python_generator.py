def simple_generator(start, end):
    current = start
    while current < end:
        yield current
        current += 1


def simple_generator_v2(start, end):
    current = start
    while current < end:
        print(current)
        yield current
        current += 1


for num in simple_generator(0, 5):
    print(num)

# Или можем воспользоваться функцией next:

test = simple_generator_v2(0, 2)
next(test)
next(test)


# next(test)  # StopIteration error


def fibonacci(number):
    a = b = 1
    for _ in range(number):
        yield a
        a, b = b, a + b


for num in fibonacci(5):
    print(num)
