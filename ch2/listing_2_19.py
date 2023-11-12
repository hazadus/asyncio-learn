"""
Счетный код и длительная задача

Sample output:
Calling <function main at 0x104cc76d0> with arguments () {}
Calling <function cpu_bound_work at 0x104732f80> with arguments () {}
<function cpu_bound_work at 0x104732f80> completed in 3.8624 sec.
Calling <function cpu_bound_work at 0x104732f80> with arguments () {}
<function cpu_bound_work at 0x104732f80> completed in 3.8587 sec.
Starting sleep for 4 sec...
End sleeping for 4 sec.
<function main at 0x104cc76d0> completed in 11.7227 sec.
"""
import asyncio

from util import async_timed, delay


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
    delay_task = asyncio.create_task(delay(4))

    await task1
    await task2
    await delay_task


asyncio.run(main())
