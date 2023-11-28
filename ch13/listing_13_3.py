"""
Демонстрация читателя стандартного вывода
"""
import asyncio
from asyncio import StreamReader
from asyncio.subprocess import Process


async def write_output(prefix: str, stdout: StreamReader):
    while line := await stdout.readline():
        print(f"[{prefix}]: {line.rstrip().decode()}")


async def main():
    program = ["ls", "-al"]
    process: Process = await asyncio.create_subprocess_exec(
        *program,
        stdout=asyncio.subprocess.PIPE,
    )

    print(f"Process PID: {process.pid}")
    stdout_task = asyncio.create_task(
        write_output(
            prefix=" ".join(program),
            stdout=process.stdout,
        )
    )
    return_code, _ = await asyncio.gather(process.wait(), stdout_task)
    print(f"{return_code=}")


asyncio.run(main())
