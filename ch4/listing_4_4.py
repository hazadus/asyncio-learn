"""
Неправильное использование спискового включения для создания и ожидания задач
"""
import asyncio

from util import async_timed, delay


@async_timed()
async def main() -> None:
    delay_times = [3, 2, 1]
    [await asyncio.create_task(delay(seconds)) for seconds in delay_times]


asyncio.run(main())
