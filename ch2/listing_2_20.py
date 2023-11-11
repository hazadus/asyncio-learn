"""
Неправильное использование блокирующего API как сопрограммы
"""
import asyncio
import requests
from util import async_timed


@async_timed()
async def get_site_status() -> int:
    return requests.get("https://hazadus.ru").status_code


@async_timed()
async def main() -> None:
    task1 = asyncio.create_task(get_site_status())
    task2 = asyncio.create_task(get_site_status())
    task3 = asyncio.create_task(get_site_status())

    await task1
    await task2
    await task3


asyncio.run(main())
