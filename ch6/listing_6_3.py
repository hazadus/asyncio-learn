"""
Асинхронное получение результатов от пула процессов
"""
from multiprocessing import Pool


def say_hello(name: str) -> str:
    return f"Hello, {name}!"


if __name__ == "__main__":
    with Pool() as process_pool:
        hi_jeff = process_pool.apply_async(say_hello, args=("Jeff",))
        hi_mills = process_pool.apply_async(say_hello, args=("Mills",))
        print(hi_jeff.get())
        print(hi_mills.get())
