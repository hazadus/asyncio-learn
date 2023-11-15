"""
Потоковая обработка результатов
"""
import asyncio

import asyncpg

from util import async_timed


@async_timed()
async def main() -> None:
    connection = await asyncpg.connect(
        host="127.0.0.1",
        port=5432,
        user="postgres",
        password="postgres",
        database="products",
    )

    query = "SELECT product_id, product_name FROM product"

    async with connection.transaction():
        async for product in connection.cursor(query):
            print(product)

    await connection.close()


asyncio.run(main())
