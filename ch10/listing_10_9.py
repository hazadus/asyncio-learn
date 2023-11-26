"""
Сопрограмма `retry`
"""
import asyncio
import logging
from typing import Awaitable, Callable


class TooManyRetries(Exception):
    pass


async def retry(
    coro: Callable[[], Awaitable],
    max_retries: int,
    timeout: float,
    retry_interval: float,
) -> None:
    for retry_num in range(0, max_retries):
        try:
            return await asyncio.wait_for(coro(), timeout=timeout)
        except Exception as ex:
            logging.exception(
                f"Exception has occured (retry {retry_num}), trying again.",
                exc_info=ex,
            )
            await asyncio.sleep(retry_interval)
    raise TooManyRetries()
