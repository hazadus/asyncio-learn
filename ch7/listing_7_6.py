"""
Использование исполнителя по умолчанию
"""
import asyncio
import functools

import requests

from util import async_timed


def get_status_code(_url: str) -> int:
    response = requests.get(_url)
    return response.status_code


@async_timed()
async def main() -> None:
    loop = asyncio.get_running_loop()

    urls = ["https://hazadus.ru" for _ in range(100)]
    tasks = [
        # None – use default thread pool executor
        loop.run_in_executor(None, functools.partial(get_status_code, url))
        for url in urls
    ]
    results = await asyncio.gather(*tasks)
    print(results)


asyncio.run(main())
