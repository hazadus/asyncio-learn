"""
Конкурентное выполнение запросов с помощью gather
"""
import asyncio

from aiohttp import ClientSession, ClientTimeout

from util import async_timed


@async_timed()
async def fetch_status(session: ClientSession, url: str) -> int:
    # Set timeout for this request:
    async with session.get(url, timeout=ClientTimeout(total=30)) as result:
        return result.status


@async_timed()
async def main() -> None:
    async with ClientSession() as session:
        urls = ["https://hazadus.ru" for _ in range(300)]
        requests = [fetch_status(session, url) for url in urls]
        status_codes = await asyncio.gather(*requests)
        print(status_codes)


asyncio.run(main())
