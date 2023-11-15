"""
Создание пула процессов
"""
import multiprocessing
from multiprocessing import Pool


def say_hello(name: str) -> str:
    return f"Hello, {name}!"


if __name__ == "__main__":
    print("CPU Cores count:", multiprocessing.cpu_count())

    with Pool() as process_pool:
        hi_jeff = process_pool.apply(say_hello, args=("Jeff",))
        hi_mills = process_pool.apply(say_hello, args=("Mills",))

        print(hi_jeff)
        print(hi_mills)
