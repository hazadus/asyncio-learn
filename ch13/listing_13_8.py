"""
Подпроцессы и семафор
"""
import asyncio
import os
import random
import string
import time
from asyncio import Semaphore
from asyncio.subprocess import Process


async def encrypt(sem: Semaphore, text: str) -> bytes:
    program = [
        "gpg",
        "-c",
        "--batch",
        "--passphrase",
        "3ncryptm3",
        "--cipher-algo",
        "TWOFISH",
    ]
    async with sem:
        process: Process = await asyncio.create_subprocess_exec(
            *program,
            stdout=asyncio.subprocess.PIPE,
            stdin=asyncio.subprocess.PIPE,
        )
        stdout, stderr = await process.communicate(text.encode())
        return stdout


async def main():
    text_list = [
        "".join(random.choice(string.ascii_letters) for _ in range(1024))
        for _ in range(100)
    ]
    # Set semaphore limit to CPU cores count:
    semaphore = Semaphore(os.cpu_count())

    s = time.time()
    tasks = [asyncio.create_task(encrypt(semaphore, text)) for text in text_list]
    encrypted_text = await asyncio.gather(*tasks)
    e = time.time()

    print(encrypted_text)
    print(f"Completed in: {e-s:.4f} sec.")


asyncio.run(main())
