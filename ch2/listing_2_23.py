"""
Выполнение счетного кода в отладочном режиме
"""
import asyncio

from util import async_timed


@async_timed()
async def cpu_bound_work() -> int:
    counter = 0
    for i in range(10**8):
        counter += 1
    return counter


async def main() -> None:
    loop = asyncio.get_event_loop()
    loop.slow_callback_duration = 0.250
    task1 = asyncio.create_task(cpu_bound_work())
    await task1


asyncio.run(main(), debug=True)
