"""
Тестирование сопрограммы `retry`
"""
import asyncio
from ch10.listing_10_9 import retry, TooManyRetries


async def main() -> None:
    async def always_fail():
        raise Exception("Failed, as usual.")

    async def always_timeout():
        await asyncio.sleep(1)

    try:
        await retry(always_fail, max_retries=3, timeout=0.1, retry_interval=0.1)
    except TooManyRetries:
        print("Too many retries!")

    try:
        await retry(always_timeout, max_retries=3, timeout=0.1, retry_interval=0.1)
    except TooManyRetries:
        print("Too many retries!")


asyncio.run(main())
