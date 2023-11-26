"""
Иллюстрация условий
"""
import asyncio
from asyncio import Condition


async def do_work(condition: Condition):
    while True:
        print("Waiting for condition...")
        async with condition:
            print("Lock acquired, releasing and waiting for condition...")
            await condition.wait()
            print("Condition met, acquiring lock again and starting to work...")
            await asyncio.sleep(1)
        print("Work is done, lock released.")


async def fire_event(condition: Condition):
    while True:
        await asyncio.sleep(5)
        print("Acquire condition before notifying...")
        async with condition:
            print("Lock acquired, notifying workers...")
            condition.notify_all()
        print("Workers notified, releasing lock.")


async def main():
    condition = Condition()
    asyncio.create_task(fire_event(condition))
    await asyncio.gather(
        do_work(condition),
        do_work(condition),
    )


asyncio.run(main())
