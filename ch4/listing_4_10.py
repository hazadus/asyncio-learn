"""
Изучение поведения `wait` по умолчанию
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
            asyncio.create_task(fetch_status(session, "https://hazadus.ru")),
            asyncio.create_task(fetch_status(session, "https://hazadus.ru/repos/")),
        ]

        done, pending = await asyncio.wait(fetchers)

        print(f"Done tasks...: {len(done)}")
        print(f"Pending tasks: {len(pending)}")

        for done_task in done:
            result = await done_task
            print(f"{result=}")


asyncio.run(main())
