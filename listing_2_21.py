"""
Создание цикла событий вручную
"""
import asyncio
from util import async_timed


@async_timed()
async def main() -> None:
    await asyncio.sleep(1)


loop = asyncio.new_event_loop()

try:
    loop.run_until_complete(main())
finally:
    loop.close()
