"""
Вложенная транзакция
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

    async with connection.transaction():
        insert_brand = "INSERT INTO brand VALUES(DEFAULT, 'my_new_brand')"
        await connection.execute(insert_brand)

        try:
            async with connection.transaction():
                await connection.execute("INSERT INTO product_color VALUES(1, 'black')")
        except Exception as ex:
            logging.exception("Error occured during transaction.", exc_info=ex)

    await connection.close()


asyncio.run(main())
