"""
Перемещение по курсору и выборка записей
"""
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

    query = "SELECT product_id, product_name FROM product"

    async with connection.transaction():
        cursor = await connection.cursor(query)
        # Move cursor 500 rows forward:
        await cursor.forward(500)
        # Fetch 100 rows starting from row #501:
        products = await cursor.fetch(100)
        for product in products:
            print(product)

    await connection.close()


asyncio.run(main())
