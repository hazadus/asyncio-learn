"""
Попытка конкурентного выполнения счетного кода

Sample output:
Calling <function main at 0x10506f760> with arguments () {}
Calling <function cpu_bound_work at 0x104afc700> with arguments () {}
<function cpu_bound_work at 0x104afc700> completed in 3.8897 sec.
Calling <function cpu_bound_work at 0x104afc700> with arguments () {}
<function cpu_bound_work at 0x104afc700> completed in 3.8725 sec.
<function main at 0x10506f760> completed in 7.7624 sec.
"""
import asyncio

from util import async_timed


@async_timed()
async def cpu_bound_work() -> int:
    counter = 0
    for i in range(10**8):
        counter += 1
    return counter


@async_timed()
async def main() -> None:
    task1 = asyncio.create_task(cpu_bound_work())
    task2 = asyncio.create_task(cpu_bound_work())

    await task1
    await task2


asyncio.run(main())
