from concurrent.futures import ThreadPoolExecutor, as_completed
import time


def f(a):
    return a * a


# parallel run
# .shutdown() in exit
t0 = time.time()
parallel_result_list = []
with ThreadPoolExecutor(max_workers=8) as pool:
    results = [pool.submit(f, i) for i in range(1_000_000)]
    for future in as_completed(results):
        parallel_result_list.append(future.result())
        # print(future.result())
print('Время выполнения параллельного кода: {}'.format(time.time() - t0))

# serial run
t0 = time.time()
serial_result_list = []
[serial_result_list.append(f(i)) for i in range(1_000_000)]
print('Время выполнения последовательного кода: {}'.format(time.time() - t0))
