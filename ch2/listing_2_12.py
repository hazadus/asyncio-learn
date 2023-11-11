"""
Задание тайм-аута для задачи с помощью `wait_for`
"""
import asyncio
from util import delay


async def main() -> None:
    delay_task = asyncio.create_task(delay(3))

    try:
        result = await asyncio.wait_for(delay_task, timeout=1)
        print(result)
    except asyncio.exceptions.TimeoutError:
        print("Timeout!")
        print("Task was cancelled?", delay_task.cancelled())


asyncio.run(main())
