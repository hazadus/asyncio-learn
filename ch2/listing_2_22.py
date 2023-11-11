"""
Получение доступа к циклу событий
"""
import asyncio
from util import delay


def call_later() -> None:
    print("I will be called soon!")


async def main() -> None:
    loop = asyncio.get_running_loop()
    loop.call_soon(call_later)
    await delay(1)


asyncio.run(main())
