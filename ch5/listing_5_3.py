"""
Использование сопрограммы `execute` для выполнения команд `create`
"""
import asyncio

import asyncpg
from listing_5_2 import (
    COLOR_INSERT,
    CREATE_BRAND_TABLE,
    CREATE_PRODUCT_COLOR_TABLE,
    CREATE_PRODUCT_SIZE_TABLE,
    CREATE_PRODUCT_TABLE,
    CREATE_SKU_TABLE,
    SIZE_INSERT,
)


async def main() -> None:
    connection = await asyncpg.connect(
        host="127.0.0.1",
        port=5432,
        user="postgres",
        database="products",
        password="postgres",
    )
    version = connection.get_server_version()
    print(f"Connected to Postgres {version=}")

    statements = [
        CREATE_BRAND_TABLE,
        CREATE_PRODUCT_TABLE,
        CREATE_PRODUCT_COLOR_TABLE,
        CREATE_PRODUCT_SIZE_TABLE,
        CREATE_SKU_TABLE,
        SIZE_INSERT,
        COLOR_INSERT,
    ]

    print("Creating tables in 'products' database...")

    for statement in statements:
        print(statement)
        status = await connection.execute(statement)
        print(f"{status=}")

    print("Tables were created.")
    await connection.close()


asyncio.run(main())
