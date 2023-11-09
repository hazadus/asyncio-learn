"""
Использование await для ожидания результата сопрограммы
"""
import asyncio


async def add_one(number: int) -> int:
    return number + 1


async def main() -> None:
    one_plus_one = await add_one(1)  # Stop and wait for result...
    two_plus_one = await add_one(2)  # Stop again, and wait for result, too...
    print(one_plus_one, two_plus_one)


asyncio.run(main())
