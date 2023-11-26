"""
Освобождений больше, чем захватов
"""
import asyncio
from asyncio import Semaphore


async def acquire(semaphore: Semaphore):
    print("Waiting to acquire the semaphore...")
    async with semaphore:
        print("Semaphore acquired")
        await asyncio.sleep(5)
    print("Semaphore released")


async def release(semaphore: Semaphore):
    print("Single release!")
    semaphore.release()
    print("Single release - complete!")


async def main():
    semaphore = Semaphore(2)

    print("Two acquisitions, three releases...")
    await asyncio.gather(acquire(semaphore), acquire(semaphore), release(semaphore))
    print("Three acquisitions...")
    await asyncio.gather(acquire(semaphore), acquire(semaphore), acquire(semaphore))


asyncio.run(main())
