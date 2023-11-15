"""
Получение заданного числа элементов с помощью асинхронного генератора
"""
import asyncio

import asyncpg


async def take(generator, to_take: int):
    item_count = 0
    async for item in generator:
        if item_count > to_take - 1:
            return
        item_count += 1
        yield item


import asyncio

import asyncpg


async def main() -> None:
    connection = await asyncpg.connect(
        host="127.0.0.1",
        port=5432,
        user="postgres",
        password="postgres",
        database="products",
    )

    async with connection.transaction():
        query = "SELECT product_id, product_name from product"
        product_generator = connection.cursor(query)

        async for product in take(product_generator, 5):
            print(product)

    await connection.close()


asyncio.run(main())
