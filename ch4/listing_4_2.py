"""
Отправка веб-запроса с по мощью aiohttp
"""
import asyncio

from aiohttp import ClientSession

from util import async_timed


@async_timed()
async def fetch_status(session: ClientSession, url: str) -> int:
    async with session.get(url) as result:
        return result.status


@async_timed()
async def main() -> None:
    async with ClientSession() as session:
        url = "https://hazadus.ru/repos/"
        status = await fetch_status(session, url)
        print(f"Status of {url} is '{status}'")


asyncio.run(main())
