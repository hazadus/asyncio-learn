"""
Инициализация пула процессов
"""
import asyncio
from concurrent.futures import ProcessPoolExecutor
from multiprocessing import Value

shared_counter: Value


def init(counter: Value) -> None:
    global shared_counter
    shared_counter = counter


def increment() -> None:
    with shared_counter.get_lock():
        shared_counter.value += 1


async def main() -> None:
    counter = Value("d", 0)  # "d" means double?..

    with ProcessPoolExecutor(initializer=init, initargs=(counter,)) as pool:
        await asyncio.get_running_loop().run_in_executor(pool, increment)
        print(f"{counter.value=}")


if __name__ == "__main__":
    asyncio.run(main())
