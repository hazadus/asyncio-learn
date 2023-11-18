"""
Выполнение запросов с помощью пула потоков
"""
import threading
import time
from concurrent.futures import ThreadPoolExecutor

import requests


def get_status_code(_url: str) -> int:
    response = requests.get(_url)
    return response.status_code


# Sync version:
urls = ["https://hazadus.ru" for _ in range(100)]

start = time.time()

for index, url in enumerate(urls):
    print(index, "(sync):", get_status_code(url))

end = time.time()
sync_time = end - start

print(f"Sync requests completed in {sync_time:.4f} sec")

# Multi-threaded version:
start = time.time()

with ThreadPoolExecutor() as pool:
    results = pool.map(get_status_code, urls)
    print("Active threads:", threading.active_count())
    for index, result in enumerate(results):
        print(index, "(threads):", result)

end = time.time()
threads_time = end - start

print(f"Threads requests completed in {threads_time:.4f} sec")

# Result comparison:
print(f"{threads_time=:.4f} vs. {sync_time=:.4f}")
