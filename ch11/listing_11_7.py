"""
Ограничение числа запросов к API с помощью семафора
"""
import asyncio
from asyncio import Semaphore

from aiohttp import ClientSession

from util import async_timed


@async_timed()
async def get_url(url: str, session: ClientSession, semaphore: Semaphore):
    print("Waiting to acquire semaphore...")
    async with semaphore:
        print("Semaphore acquired, sending request...")
        response = await session.get(url)
        print("Request completed.")
        return response.status


@async_timed()
async def main():
    semaphore = Semaphore(10)
    async with ClientSession() as session:
        tasks = [get_url("https://hazadus.ru", session, semaphore) for _ in range(1000)]
        await asyncio.gather(*tasks)


asyncio.run(main())
