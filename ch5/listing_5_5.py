"""
Вставка случайных марок
"""
import asyncio
from random import sample
from typing import List, Tuple, Union

import asyncpg


def load_common_words() -> List[str]:
    with open("common_words.txt") as file:
        return file.readlines()


def generate_brand_names(words: List[str]) -> List[Tuple[Union[str,]]]:
    return [(words[index].capitalize(),) for index in sample(range(100), 100)]


async def insert_brands(common_words: List[str], connection) -> int:
    brands = generate_brand_names(common_words)
    insert_statement = "INSERT INTO brand VALUES(DEFAULT, $1)"
    return await connection.executemany(insert_statement, brands)


async def main() -> None:
    common_words = load_common_words()
    connection = await asyncpg.connect(
        host="127.0.0.1",
        port=5432,
        user="postgres",
        database="products",
        password="postgres",
    )
    result = await insert_brands(common_words, connection)
    print(f"{result=}")


asyncio.run(main())
