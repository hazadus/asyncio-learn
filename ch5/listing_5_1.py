"""
Подключение к базе данных Postgres от имени пользователя по умолчанию
"""
import asyncpg
import asyncio


async def main() -> None:
    connection = await asyncpg.connect(
        host="127.0.0.1",
        port=5432,
        user="postgres",
        database="postgres",
        password="postgres",
    )
    version = connection.get_server_version()
    print(f"Connected to Postgres {version=}")
    await connection.close()


asyncio.run(main())
