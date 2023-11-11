"""
Ожидание будущего объекта
"""
import asyncio
from asyncio import Future


def make_request() -> Future:
    future = Future()
    # Create task that will set future value asynchronously:
    asyncio.create_task(set_future_value(future))
    return future


async def set_future_value(future: Future) -> None:
    await asyncio.sleep(1)
    future.set_result(42)


async def main():
    future = make_request()
    print(f"Future object ready? {future.done()}")
    print(f"future = {future}")
    value = await future  # Pause `main` until future value is set
    print(f"Future object ready? {future.done()}")
    print(f"future = {future}")
    print(f"value = {value}")


asyncio.run(main())
