# Ускорение кода Python
GIL (Global Interpreter Lock) - это механизм, который блокирует выполнение одного и того же байтокода нескольким потокам одновременно. 
Но это не говорит о том, что в Python невозможны паралелльные вычисления. 

Для параллелизации вычислений в Python могут быть использованы библиотеки:

[**1.Threading**](https://github.com/devFF/FindJob/tree/main/Acceleration/Threading) - многопоточные вычисления (I/O bound задачи)

[**2.Multiprocessing**](https://github.com/devFF/FindJob/tree/main/Acceleration/Multiprocessing) - многопроцессорные вычисления (CPU-bound задачи)

[**3.Asyncio**](https://github.com/devFF/FindJob/tree/main/Acceleration/Multiprocessing) - асинхронное программирование

Отдельно стоит обратить внимание на библиотеку [Taichi](https://github.com/devFF/FindJob/tree/main/Acceleration/Taichi), позволяющую ускорить выполнение кода Python на 1-2 порядка!



