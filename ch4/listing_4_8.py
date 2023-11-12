"""
Использование `as_completed`
"""
import asyncio
from aiohttp import ClientSession, ClientTimeout
from util import async_timed


@async_timed()
async def fetch_status(session: ClientSession, url: str, delay: int = 0) -> int:
    await asyncio.sleep(delay)
    # Set timeout for this request:
    async with session.get(url, timeout=ClientTimeout(total=30)) as result:
        return result.status


@async_timed()
async def main() -> None:
    async with ClientSession() as session:
        fetchers = [
            fetch_status(session, "https://hazadus.ru", 1),
            fetch_status(session, "https://hazadus.ru", 3),
            fetch_status(session, "https://hazadus.ru", 7),
        ]

        for finished_task in asyncio.as_completed(fetchers):
            print(await finished_task)


asyncio.run(main())
