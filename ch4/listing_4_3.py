"""
Задание тайм-аутов в aiohttp
"""
import asyncio
from aiohttp import ClientSession, ClientTimeout
from util import async_timed


@async_timed()
async def fetch_status(session: ClientSession, url: str) -> int:
    # Set timeout for this request:
    async with session.get(url, timeout=ClientTimeout(total=0.01)) as result:
        return result.status


@async_timed()
async def main() -> None:
    # Set full (total) timeout and connection timeout separately:
    async with ClientSession(timeout=ClientTimeout(total=1, connect=0.1)) as session:
        url = "https://hazadus.ru/repos/"
        status = await fetch_status(session, url)
        print(f"Status of {url} is '{status}'")


asyncio.run(main())
