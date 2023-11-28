"""
Завершение подпроцесса
"""
import asyncio
from asyncio.subprocess import Process


async def main():
    process: Process = await asyncio.create_subprocess_exec("sleep", "3")
    print(f"Process pid: {process.pid}")
    try:
        status_code = await asyncio.wait_for(process.wait(), timeout=1.0)
        print(f"{status_code=}")
    except asyncio.TimeoutError:
        print("Timeout, stopping the process...")
        process.terminate()
        status_code = await process.wait()
        print(f"{status_code=}")


asyncio.run(main())
