"""
Принудительный запуск итерации цикла событий
"""
import asyncio
from util import delay


async def create_tasks_no_sleep():
    task1 = asyncio.create_task(delay(1))
    task2 = asyncio.create_task(delay(2))
    print("Applying gather() to tasks:")
    await asyncio.gather(task1, task2)


async def create_tasks_sleep():
    task1 = asyncio.create_task(delay(1))
    await asyncio.sleep(0)
    task2 = asyncio.create_task(delay(2))
    await asyncio.sleep(0)
    print("Applying gather() to tasks:")
    await asyncio.gather(task1, task2)


async def main():
    print("=" * 10, "Without asyncio.sleep(0)", "=" * 10)
    await create_tasks_no_sleep()
    print("=" * 10, "With asyncio.sleep(0)", "=" * 13)
    await create_tasks_sleep()


asyncio.run(main())
