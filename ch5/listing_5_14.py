"""
Простой асинхронный генератор
"""
import asyncio

from util import async_timed, delay


async def positive_integers_async(until: int):
    """
    This will return an async_generator.
    """
    for integer in range(1, until):
        await delay(integer)
        yield integer


@async_timed()
async def main() -> None:
    async_generator = positive_integers_async(3)
    print(type(async_generator))
    # `async for` should be used to iterate over async generator:
    async for number in async_generator:
        print(f"Got {number=}")


asyncio.run(main())
