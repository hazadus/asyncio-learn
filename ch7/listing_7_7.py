"""
Использование сопрограммы `to_thread`
"""
import asyncio

import requests

from util import async_timed


def get_status_code(_url: str) -> int:
    response = requests.get(_url)
    return response.status_code


@async_timed()
async def main() -> None:
    urls = ["https://hazadus.ru" for _ in range(100)]
    # Run get_status_code in a separate thread:
    tasks = [asyncio.to_thread(get_status_code, url) for url in urls]
    results = await asyncio.gather(*tasks)
    print(results)


asyncio.run(main())
