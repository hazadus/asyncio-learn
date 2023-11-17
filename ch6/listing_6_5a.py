"""
Исполнитель пула процессов в сочетании с `asyncio.as_completed()`
"""
import asyncio
from asyncio.events import AbstractEventLoop
from concurrent.futures import ProcessPoolExecutor
from functools import partial
from typing import List


def count(count_to: int) -> int:
    counter = 0
    while counter < count_to:
        counter += 1
    return counter


async def main() -> None:
    with ProcessPoolExecutor() as process_pool:
        loop: AbstractEventLoop = asyncio.get_running_loop()
        nums = [10**8, 1, 3, 5, 22]
        calls: List[partial[int]] = [partial(count, num) for num in nums]
        call_coros = []

        for call in calls:
            call_coros.append(loop.run_in_executor(process_pool, call))

        # Print result as soon as it's ready:
        for finished_task in asyncio.as_completed(call_coros, timeout=3):
            try:
                result = await finished_task
                print(f"{result=}")
            except asyncio.TimeoutError:
                print("Timeout!")


if __name__ == "__main__":
    asyncio.run(main())
