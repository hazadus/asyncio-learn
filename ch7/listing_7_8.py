"""
Печать информации о состоянии отправки запросов
"""
import asyncio
import functools
from concurrent.futures import ThreadPoolExecutor
from threading import Lock

import requests

from util import async_timed

REQUEST_COUNT = 100
counter_lock = Lock()
counter: int = 0


def get_status_code(_url: str) -> int:
    global counter
    response = requests.get(_url)
    with counter_lock:
        counter += 1
    return response.status_code


async def reporter(request_count: int):
    while counter < request_count:
        print(f"Requests completed: {counter} of {request_count}")
        await asyncio.sleep(0.5)


@async_timed()
async def main() -> None:
    loop = asyncio.get_running_loop()

    with ThreadPoolExecutor() as pool:
        urls = ["https://hazadus.ru" for _ in range(REQUEST_COUNT)]
        reporter_task = asyncio.create_task(reporter(REQUEST_COUNT))
        tasks = [
            loop.run_in_executor(pool, functools.partial(get_status_code, url))
            for url in urls
        ]
        results = await asyncio.gather(*tasks)
        await reporter_task
        print(results)


asyncio.run(main())
