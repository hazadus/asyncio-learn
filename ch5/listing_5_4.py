"""
Вставка и выборка марок
"""
import asyncio
from typing import List

import asyncpg
from asyncpg import Record


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

    await connection.execute("INSERT INTO brand VALUES(DEFAULT, 'Levis')")
    await connection.execute("INSERT INTO brand VALUES(DEFAULT, 'Seven')")

    brand_query = "SELECT brand_id, brand_name FROM brand"
    results: List[Record] = await connection.fetch(brand_query)

    for brand in results:
        print(f"{brand=}")

    await connection.close()


asyncio.run(main())
