"""
Использование `communicate` со стандартным вводом
"""
import asyncio
from asyncio.subprocess import Process


async def main():
    program = ["python3", "listing_13_9.py"]
    process: Process = await asyncio.create_subprocess_exec(
        *program,
        stdout=asyncio.subprocess.PIPE,
        stdin=asyncio.subprocess.PIPE,
    )
    stdout, stderr = await process.communicate(b"Hazadus")
    print(f"{stdout=}")
    print(f"{stderr=}")


asyncio.run(main())
