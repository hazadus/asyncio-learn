"""
Использование тайм-аутов в `wait`
"""
import asyncio
from aiohttp import ClientSession
from util import async_timed


@async_timed()
async def fetch_status(session: ClientSession, url: str, delay: int = 0) -> int:
    await asyncio.sleep(delay)
    async with session.get(url) as result:
        return result.status


@async_timed()
async def main() -> None:
    async with ClientSession() as session:
        fetchers = [
            asyncio.create_task(fetch_status(session, url="https://hazadus.ru")),
            asyncio.create_task(fetch_status(session, url="https://hazadus.ru")),
            asyncio.create_task(fetch_status(session, "https://hazadus.ru", delay=3)),
        ]

        done, pending = await asyncio.wait(fetchers, timeout=1)

        print(f"Done tasks...: {len(done)}")
        print(f"Pending tasks: {len(pending)}")

        for done_task in done:
            print(await done_task)


asyncio.run(main())
