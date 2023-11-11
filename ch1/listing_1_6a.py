"""
Многопроцессное вычисление последовательности чисел Фибоначчи (нет в книге)

Example output:
fib(40) = 63245986
fib(41) = 102334155
Exection time: 33.1269 sec.
"""
import multiprocessing
import time


def print_fib(number: int) -> None:
    def fib(n: int) -> int:
        if n == 1:
            return 0
        elif n == 2:
            return 1
        else:
            return fib(n - 1) + fib(n - 2)

    print(f"fib({number}) = {fib(n=number)}")


def fibs_with_processess():
    thread40 = multiprocessing.Process(target=print_fib, args=(40,))
    thread41 = multiprocessing.Process(target=print_fib, args=(41,))

    thread40.start()
    thread41.start()

    thread40.join()
    thread41.join()


# "main" idiom is needed for `multiprocessing` to work correctly.
if __name__ == "__main__":
    start = time.time()
    fibs_with_processess()
    end = time.time()
    print(f"Exection time: {end - start:.4f} sec.")
