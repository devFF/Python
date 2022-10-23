import threading
import time


def cpu_bound(n):
    while n >= 0:
        n -= 1


def io_bound(n):
    while n >= 0:
        n -= 1
        with open('file.txt', 'w') as f:
            f.write(str(n))


# Последовательный (serial) код - CPU bound
n = 100_000_000
time_start = time.time()
cpu_bound(n)
cpu_bound(n)
print('CPU-bound serial run:{}'.format(time.time() - time_start))

# Многопоточный (parallel) код - CPU bound
time_start = time.time()
run1 = threading.Thread(target=cpu_bound, args=(n,))
run2 = threading.Thread(target=cpu_bound, args=(n,))
run1.start()
run2.start()
run1.join()
run2.join()
print('CPU-bound parallel run:{}'.format(time.time() - time_start))

# Последовательный (serial) код - I/O bound
n = 100_000
time_start = time.time()
io_bound(n)
io_bound(n)
print('I/O bound serial run:{}'.format(time.time() - time_start))

# Многопоточный (parallel) код - I/O bound
time_start = time.time()
run1 = threading.Thread(target=io_bound, args=(n,))
run2 = threading.Thread(target=io_bound, args=(n,))
run1.start()
run2.start()
run1.join()
run2.join()
print('I/O bound parallel run:{}'.format(time.time() - time_start))
