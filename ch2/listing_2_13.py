"""
Защита задачи от снятия
"""
import asyncio

from util import delay


async def main() -> None:
    delay_task = asyncio.create_task(delay(10))

    try:
        result = await asyncio.wait_for(asyncio.shield(delay_task), timeout=5)
        print(result)
    except asyncio.exceptions.TimeoutError:
        print("Task taken more than 5 sec, it will end soon!")
        result = await delay_task
        print(result)


asyncio.run(main())
