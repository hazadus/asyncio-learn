"""
Использование потоковых читателей для ввода данных
"""
import asyncio

from ch8.listing_8_5 import create_stdin_reader
from util import delay


async def main() -> None:
    stdin_reader = await create_stdin_reader()
    while True:
        delay_time = await stdin_reader.readline()
        asyncio.create_task(delay(int(delay_time)))


asyncio.run(main())
