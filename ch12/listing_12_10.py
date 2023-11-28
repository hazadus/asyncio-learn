"""
LIFO-очередь
"""
import asyncio
from asyncio import LifoQueue, Queue
from dataclasses import dataclass, field


@dataclass(order=True)
class WorkItem:
    priority: int
    order: int
    data: str = field(compare=False)


async def worker(queue: Queue):
    while not queue.empty():
        work_item: WorkItem = await queue.get()
        print(f"Processing element {work_item}")
        queue.task_done()


async def main():
    lifo_queue = LifoQueue()

    work_items = [
        WorkItem(3, 1, "Lowest priority 1"),
        WorkItem(3, 2, "Lowest priority 2"),
        WorkItem(3, 3, "Lowest priority 3"),
        WorkItem(2, 4, "Medium priority"),
        WorkItem(1, 5, "High priority"),
    ]

    worker_task = asyncio.create_task(worker(lifo_queue))

    for work in work_items:
        lifo_queue.put_nowait(work)

    await asyncio.gather(lifo_queue.join(), worker_task)


asyncio.run(main())
