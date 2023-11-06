"""
Синхронное чтение кода состояния
"""
import time
import requests


def read_example() -> None:
    response = requests.get("https://hazadus.ru")
    print(response.status_code)


start = time.time()

read_example()
read_example()

end = time.time()

print(f"Execution time: {end - start:.4f} sec.")
