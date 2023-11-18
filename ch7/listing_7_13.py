"""
Класс нагрузочного тестирования
"""
import asyncio
from asyncio import AbstractEventLoop
from concurrent.futures import Future
from typing import Callable, Optional

from aiohttp import ClientSession


class StressTest:
    def __init__(
        self,
        loop: AbstractEventLoop,
        url: str,
        total_requests: int,
        callback: Callable[[int, int], None],
    ):
        self._completed_requests: int = 0
        self._load_test_future: Optional[Future] = None
        self._loop = loop
        self._url = url
        self._total_requests = total_requests
        self._callback = callback  # Progress reporter
        self._refresh_rate = total_requests // 100

    def start(self):
        # Save future object in case we need to cancel test before it finishes:
        future = asyncio.run_coroutine_threadsafe(self._make_requests(), self._loop)
        self._load_test_future = future

    def cancel(self):
        if self._load_test_future:
            self._loop.call_soon_threadsafe(self._load_test_future.cancel)

    async def _get_url(self, session: ClientSession, url: str) -> None:
        try:
            await session.get(url)
        except Exception as ex:
            print(ex)

        # We do not need to use lock, because asyncio works in single thread.
        # There will be no race conditions.
        self._completed_requests += 1

        # Call callback function to report progress on each 1% of completed requests
        if (
            self._completed_requests % self._refresh_rate == 0
            or self._completed_requests == self._total_requests
        ):
            self._callback(self._completed_requests, self._total_requests)

    async def _make_requests(self):
        async with ClientSession() as session:
            reqs = [
                self._get_url(session, self._url) for _ in range(self._total_requests)
            ]
        await asyncio.gather(*reqs)
