"""
Попытка выполнения задач в фоновом режиме
"""
import asyncio

from util import delay


async def main():
    while True:
        delay_time = input("Enter time to sleep:")
        asyncio.create_task(delay(int(delay_time)))


asyncio.run(main())
