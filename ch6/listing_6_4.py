"""
Исполнители пула процессов
"""
import multiprocessing
import time
from concurrent.futures import ProcessPoolExecutor


def count(count_to: int) -> int:
    start = time.time()
    counter = 0
    while counter < count_to:
        counter += 1
    end = time.time()
    print(f"End counting to {count_to} in {end-start} sec.")
    return counter


if __name__ == "__main__":
    with ProcessPoolExecutor() as process_pool:
        print("CPU Cores count:", multiprocessing.cpu_count())

        numbers = [10**8, 1, 3, 5, 22]
        for result in process_pool.map(count, numbers):
            print(result)
