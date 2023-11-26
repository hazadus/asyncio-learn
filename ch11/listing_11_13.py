"""
Исполнитель не поспевает за событиями
"""
import asyncio
from asyncio import Event
from contextlib import suppress


async def trigger_event_periodically(event: Event):
    while True:
        print("Activating event!")
        event.set()
        await asyncio.sleep(1)


async def do_work_on_event(event: Event):
    while True:
        print("Waiting for the event...")
        await event.wait()
        event.clear()
        print("Working!")
        await asyncio.sleep(5)
        print("Work completed!")


async def main():
    event = Event()
    trigger = asyncio.wait_for(trigger_event_periodically(event), 5.0)

    with suppress(asyncio.TimeoutError):
        await asyncio.gather(
            do_work_on_event(event),
            do_work_on_event(event),
            trigger,
        )


asyncio.run(main())
