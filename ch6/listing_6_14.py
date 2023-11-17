"""
Наблюдение за ходом отображения
"""
import asyncio
import functools
from concurrent.futures import ProcessPoolExecutor
from multiprocessing import Value
from typing import Dict, List

from listing_6_8 import merge_dictionaries, partition

map_progress: Value


def init(progress: Value):
    global map_progress
    map_progress = progress


def map_frequencies(chunk: List[str]) -> Dict[str, int]:
    counter = {}
    for line in chunk:
        word, _, count, _ = line.split("\t")
        if counter.get(word):
            counter[word] = counter[word] + int(count)
        else:
            counter[word] = int(count)

    global map_progress
    with map_progress.get_lock():
        map_progress.value += 1

    return counter


async def progress_reporter(total_partitions: int) -> None:
    global map_progress
    while map_progress.value < total_partitions:
        print(f"Reduce operations complete: {map_progress.value} of {total_partitions}")
        await asyncio.sleep(0.5)


async def main(partition_size: int) -> None:
    global map_progress

    with open(
        "/Users/hazadus/Downloads/googlebooks-eng-all-1gram-20120701-a",
        encoding="utf-8",
    ) as file:
        contents = file.readlines()
        loop = asyncio.get_running_loop()
        tasks = []
        map_progress = Value("i", 0)

        with ProcessPoolExecutor(initializer=init, initargs=(map_progress,)) as pool:
            total_partitions = len(contents) // partition_size
            reporter = asyncio.create_task(progress_reporter(total_partitions))

            for chunk in partition(contents, partition_size):
                tasks.append(
                    loop.run_in_executor(
                        pool, functools.partial(map_frequencies, chunk)
                    )
                )

            counters = await asyncio.gather(*tasks)

            await reporter

            final_result = functools.reduce(merge_dictionaries, counters)
            print(f"{final_result['Aardvark']=}")


if __name__ == "__main__":
    asyncio.run(main(partition_size=50000))
