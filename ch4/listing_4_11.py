"""
Обработка исключений при использовании `wait`
"""
import asyncio
import logging

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
            asyncio.create_task(fetch_status(session, "error://hazadus.ru/repos/")),
        ]

        # `ALL_COMPLETED` is default mode!
        done, pending = await asyncio.wait(fetchers, return_when=asyncio.ALL_COMPLETED)

        print(f"Done tasks...: {len(done)}")
        print(f"Pending tasks: {len(pending)}")

        for done_task in done:
            if done_task.exception() is None:
                print(f"{done_task.result()=}")
            else:
                logging.error(
                    "An error has occured during request",
                    exc_info=done_task.exception(),
                )


asyncio.run(main())
