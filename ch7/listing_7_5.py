"""
Использование исполнителя пула потоков совместно с `asyncio`
"""
import asyncio
import functools
from concurrent.futures import ThreadPoolExecutor

import requests

from util import async_timed


def get_status_code(_url: str) -> int:
    response = requests.get(_url)
    return response.status_code


@async_timed()
async def main() -> None:
    loop = asyncio.get_running_loop()

    with ThreadPoolExecutor() as pool:
        urls = ["https://hazadus.ru" for _ in range(100)]
        tasks = [
            loop.run_in_executor(pool, functools.partial(get_status_code, url))
            for url in urls
        ]
        results = await asyncio.gather(*tasks)
        print(results)


asyncio.run(main())
