"""
Выполнение двух сопрограмм
"""
import asyncio

from util import delay


async def add_one(number: int) -> int:
    return number + 1


async def hello_message() -> str:
    await delay(1)
    return "Hello World!"


async def main() -> None:
    message = await hello_message()  # Stop `main` until return from `hello_message`...
    one_plus_one = await add_one(1)  # Stop `main` until return from `add_one`...
    print("one_plus_one =", one_plus_one)
    print(message)


asyncio.run(main())
