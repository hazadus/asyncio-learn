"""
Генерирование последовательности Фибоначчи и его хронометраж

Example output:
fib(40) = 63245986
fib(41) = 102334155
Exection time: 52.1460 sec.
"""
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


def fibs_no_threading():
    print_fib(40)
    print_fib(41)


start = time.time()

fibs_no_threading()

end = time.time()

print(f"Exection time: {end - start:.4f} sec.")
