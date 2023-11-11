"""
Хронометраж двух конкурентных задач с помощью декоратора
"""
import asyncio
from util import async_timed


@async_timed()
async def delay(delay_seconds: int) -> int:
    print(f"Starting sleep for {delay_seconds} sec...")
    await asyncio.sleep(delay_seconds)
    print(f"End sleeping for {delay_seconds} sec.")
    return delay_seconds


@async_timed()
async def main():
    task1 = asyncio.create_task(delay(2))
    task2 = asyncio.create_task(delay(3))

    await task1
    await task2


asyncio.run(main())
