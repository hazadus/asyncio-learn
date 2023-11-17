"""
Распараллеливание операции `reduce`

Sample output:
MapReduce time: 22.6181 sec
"""
import asyncio
import functools
import time
from concurrent.futures import ProcessPoolExecutor
from functools import partial
from typing import Dict, List

CHUNK_SIZE = 50000


def partition(data: List, chunk_size: int) -> List:
    for i in range(0, len(data), chunk_size):
        yield data[i : i + chunk_size]


def map_frequencies(chunk: List[str]) -> Dict[str, int]:
    counter = {}
    for line in chunk:
        word, _, count, _ = line.split("\t")
        if counter.get(word):
            counter[word] = counter[word] + int(count)
        else:
            counter[word] = int(count)
    return counter


def merge_dictionaries(first: Dict[str, int], second: Dict[str, int]) -> Dict[str, int]:
    merged = first
    for key in second:
        if key in merged:
            merged[key] = merged[key] + second[key]
        else:
            merged[key] = second[key]
    return merged


async def reduce(loop, pool, counters, chunk_size) -> Dict[str, int]:
    chunks: List[List[Dict]] = list(partition(counters, chunk_size))
    reducers = []

    while len(chunks[0]) > 1:
        for chunk in chunks:
            reducer = partial(functools.reduce, merge_dictionaries, chunk)
            reducers.append(loop.run_in_executor(pool, reducer))
        reducer_chunks = await asyncio.gather(*reducers)
        chunks = list(partition(reducer_chunks, chunk_size))
        reducers.clear()
    return chunks[0][0]


async def main() -> None:
    with open(
        "/Users/hazadus/Downloads/googlebooks-eng-all-1gram-20120701-a",
        encoding="utf-8",
    ) as file:
        contents = file.readlines()
        loop = asyncio.get_running_loop()
        tasks = []
        start = time.time()

        with ProcessPoolExecutor() as pool:
            for chunk in partition(contents, CHUNK_SIZE):
                tasks.append(
                    loop.run_in_executor(pool, partial(map_frequencies, chunk))
                )

            intermediate_results = await asyncio.gather(*tasks)
            final_result = await reduce(loop, pool, intermediate_results, 500)

        end = time.time()
        print(f"MapReduce time: {end-start:.4f} sec")


if __name__ == "__main__":
    asyncio.run(main())
