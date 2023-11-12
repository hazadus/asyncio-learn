"""
Многопоточное чтение кода состояния
"""
import threading
import time

import requests

THREADS_QTY = 10


def read_example() -> None:
    response = requests.get("https://hazadus.ru")
    print(f"{threading.current_thread().name}, status code: {response.status_code}")


thread_pool = []

# Create all threads
for i in range(0, THREADS_QTY):
    thread = threading.Thread(target=read_example)
    thread_pool.append(thread)

start = time.time()

# Start each thread
for thread in thread_pool:
    thread.start()
    print(f"Thread {thread} started.")

print("All threads started!")

# Join each thread
for thread in thread_pool:
    thread.join()

end = time.time()

print(f"Execution time: {end - start:.4f} sec.")
