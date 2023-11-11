"""
Добавление обработчика сигнала, снимающего все задачи
"""
import asyncio
import signal
from asyncio import AbstractEventLoop
from typing import Set

from util import delay


def cancel_tasks():
    print("Got SIGINT!")
    tasks: Set[asyncio.Task] = asyncio.all_tasks()
    print(f"Cancelling {len(tasks)} tasks...")
    [task.cancel() for task in tasks]


async def main():
    loop: AbstractEventLoop = asyncio.get_running_loop()
    loop.add_signal_handler(signal.SIGINT, cancel_tasks)
    await delay(10)


asyncio.run(main())
