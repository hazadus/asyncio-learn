"""
Обработка исключений при использовании gather
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
        urls = ["https://hazadus.ru", "error://hazadus.ru"]
        requests = [fetch_status(session, url) for url in urls]
        results = await asyncio.gather(*requests, return_exceptions=True)
        exceptions = [res for res in results if isinstance(res, Exception)]
        status_codes = [res for res in results if not isinstance(res, Exception)]
        print(f"{results=}")
        print(f"{exceptions=}")
        print(f"{status_codes=}")


asyncio.run(main())
