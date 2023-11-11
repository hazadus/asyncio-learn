"""
Создание задачи
"""
import asyncio
from util import delay


async def main() -> None:
    sleep3 = asyncio.create_task(delay(3))
    print("type:", type(sleep3))
    result = await sleep3
    print("result:", result)


asyncio.run(main())
