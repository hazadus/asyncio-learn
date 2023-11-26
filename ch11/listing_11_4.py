"""
Использование блокировки `asyncio`
"""
import asyncio
from asyncio import Lock
from util import delay


async def a(lock: Lock):
    print("Coro 'a' is waiting to acquire lock")
    async with lock:
        print("Coro 'a' has acquired the lock!")
        await delay(2)
    print("Coro 'a' has released the lock.")


async def b(lock: Lock):
    print("Coro 'b' is waiting to acquire lock")
    async with lock:
        print("Coro 'b' has acquired the lock!")
        await delay(2)
    print("Coro 'b' has released the lock.")


async def main():
    # NB: do not make `lock` global! (see p.310).
    lock = Lock()
    await asyncio.gather(b(lock), a(lock))


asyncio.run(main())
