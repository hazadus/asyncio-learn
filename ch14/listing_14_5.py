"""
Сопрограммы на основе генераторов
"""
import asyncio


@asyncio.coroutine  # = async def
def coroutine():
    print("Sleeping!")
    yield from asyncio.sleep(1)  # = await asyncio.sleep(1)
    print("Woke up!")


asyncio.run(coroutine())
