"""
Взаимоблокировка при использовании канала
"""
import asyncio
from asyncio.subprocess import Process


async def main():
    program = ["python3", "listing_13_4.py"]
    process: Process = await asyncio.create_subprocess_exec(
        *program,
        stdout=asyncio.subprocess.PIPE,
    )
    print(f"Process PID: {process.pid}")
    return_code = await process.wait()
    print(f"{return_code=}")


asyncio.run(main())
