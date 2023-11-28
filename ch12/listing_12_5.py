"""
Очередь с приоритетами, содержащая кортежи
"""
import asyncio
from asyncio import PriorityQueue, Queue
from typing import Tuple


async def worker(queue: Queue):
    while not queue.empty():
        work_item: Tuple[int, str] = await queue.get()
        print(f"Processing element {work_item}")
        queue.task_done()


async def main():
    priority_queue = PriorityQueue()

    work_items = [
        (3, "Lowest priority"),
        (2, "Medium priority"),
        (1, "Highest priority"),
    ]

    worker_task = asyncio.create_task(worker(priority_queue))

    for work in work_items:
        priority_queue.put_nowait(work)

    await asyncio.gather(priority_queue.join(), worker_task)


asyncio.run(main())
