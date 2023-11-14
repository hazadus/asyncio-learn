"""
Создание пула подключений и конкурентное выполнение запросов
"""
import asyncio

import asyncpg

product_query = """
    SELECT p.product_id,
    p.product_name,
    p.brand_id,
    s.sku_id,
    pc.product_color_name,
    ps.product_size_name
    FROM product as p
    JOIN sku as s on s.product_id = p.product_id
    JOIN product_color as pc on pc.product_color_id = s.product_color_id
    JOIN product_size as ps on ps.product_size_id = s.product_size_id
    WHERE p.product_id = 100
    """


async def query_product(pool):
    # Wait until we get a connection from the pool:
    async with pool.acquire() as connection:
        return await connection.fetchrow(product_query)


async def main() -> None:
    async with asyncpg.create_pool(
        host="127.0.0.1",
        port=5432,
        user="postgres",
        password="postgres",
        database="products",
        min_size=6,
        max_size=6,
    ) as pool:
        result = await asyncio.gather(
            query_product(pool),
            query_product(pool),
        )
        for record in result:
            print(record)


asyncio.run(main())
