"""
Тайм-ауты в сочетании с `as_completed`
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
            fetch_status(session, "https://hazadus.ru", 1),
            fetch_status(session, "https://hazadus.ru", 10),
            fetch_status(session, "https://hazadus.ru", 10),
        ]

        for finished_task in asyncio.as_completed(fetchers, timeout=3):
            try:
                result = await finished_task
                print(f"{result=}")
            except asyncio.TimeoutError:
                print("Timeout!")

        for task in asyncio.tasks.all_tasks():
            print(task)


asyncio.run(main())
