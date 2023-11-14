"""
Обработка ошибки в транзакции
"""
import asyncio
import logging

import asyncpg


async def main() -> None:
    connection = await asyncpg.connect(
        host="127.0.0.1",
        port=5432,
        user="postgres",
        password="postgres",
        database="products",
    )

    try:
        async with connection.transaction():
            insert_brand = "INSERT INTO brand VALUES(9999, 'big_brand')"
            await connection.execute(insert_brand)
            # INSERT with dupe primary key will fail:
            await connection.execute(insert_brand)
    except Exception as ex:
        logging.exception("Error occured during transaction.", exc_info=ex)
    finally:
        query = """
            SELECT brand_name FROM brand
            WHERE brand_name LIKE 'brand%'
        """

        brands = await connection.fetch(query)
        print(brands)

    await connection.close()


asyncio.run(main())
