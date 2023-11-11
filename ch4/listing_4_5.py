"""
Использование спискового включения для конкурентного выполнения задач
"""
import asyncio
from util import async_timed, delay


@async_timed()
async def main() -> None:
    delay_times = [3, 2, 1]
    tasks = [asyncio.create_task(delay(seconds)) for seconds in delay_times]
    [await task for task in tasks]


asyncio.run(main())
