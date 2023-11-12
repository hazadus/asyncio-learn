"""
Конкурентное выполнение нескольких задач
"""
import asyncio

from util import delay


async def main() -> None:
    sleep3 = asyncio.create_task(delay(3))
    sleep3_again = asyncio.create_task(delay(3))
    sleep3_once_more = asyncio.create_task(delay(3))

    await sleep3
    await sleep3_again
    await sleep3_once_more


asyncio.run(main())
