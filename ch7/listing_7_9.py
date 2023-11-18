"""
Блокировки и рекурсия
"""
from threading import RLock, Thread
from typing import List

list_lock = RLock()


def sum_list(int_list: List[int]) -> int:
    print("Waiting for lock...")
    # Program will freeze on second iteration.
    with list_lock:
        print("Lock acquired.")
        if len(int_list) == 0:
            print("Sum completed.")
            return 0
        else:
            head, *tail = int_list
            print("Summing the rest of the list...")
            return head + sum_list(tail)


thread = Thread(target=sum_list, args=([1, 2, 3, 4],))
thread.start()
thread.join()
