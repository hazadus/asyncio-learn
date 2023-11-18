"""
Хеширование с применением многопоточности и `asyncio`

Sample output:
Calling <function main at 0x10352d1b0> with arguments () {}
<function main at 0x10352d1b0> completed in 7.1219 sec.
"""
import asyncio
import functools
import hashlib
import os
import random
import string
from concurrent.futures import ThreadPoolExecutor

from util import async_timed


def random_password(length: int) -> str:
    ascii_lowercase = string.ascii_lowercase
    return "".join(random.choice(ascii_lowercase) for _ in range(length))


passwords = [random_password(10) for _ in range(10000)]


def hash(password: bytes) -> str:
    salt = os.urandom(16)
    return str(hashlib.scrypt(password, salt=salt, n=2048, p=1, r=8))


@async_timed()
async def main() -> None:
    loop = asyncio.get_running_loop()
    tasks = []

    with ThreadPoolExecutor() as pool:
        for password in passwords:
            tasks.append(
                loop.run_in_executor(
                    pool, functools.partial(hash, bytes(password, encoding="utf-8"))
                )
            )

    await asyncio.gather(*tasks)


asyncio.run(main())
