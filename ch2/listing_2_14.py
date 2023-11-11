"""
Основы будущих объектов
"""
from asyncio import Future

my_furure = Future()

print("my_future =", my_furure)
print(f"my_future ready? {my_furure.done()}")

my_furure.set_result(42)

print(f"my_future ready? {my_furure.done()}")
print(f"my_future.result() = {my_furure.result()}")
