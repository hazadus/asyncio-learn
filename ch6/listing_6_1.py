"""
Два параллельных процесса
p.158
"""
import time
from multiprocessing import Process


def count(count_to: int) -> int:
    start = time.time()
    counter = 0
    while counter < count_to:
        counter += 1
    end = time.time()
    print(f"End counting to {count_to} in {end-start}")
    return counter


if __name__ == "__main__":
    start_time = time.time()

    to10pow8 = Process(target=count, args=(10**8,))
    to20pow8 = Process(target=count, args=(2 * 10**8,))

    # Run two processess concurrently:
    to10pow8.start()
    to20pow8.start()

    to10pow8.join()
    to20pow8.join()

    end_time = time.time()
    print(f"Total run time {end_time-start_time}")
