"""
Создание и уничтожение пула подключений к базе данных
"""
import asyncpg
from aiohttp.web_app import Application
from asyncpg.pool import Pool

DB_KEY = "database"


async def create_database_pool(
    app: Application,
    host: str,
    port: int,
    user: int,
    database: str,
    password: str,
) -> None:
    pool: Pool = await asyncpg.create_pool(
        host=host,
        port=port,
        user=user,
        password=password,
        database=database,
        min_size=6,
        max_size=6,
    )
    app[DB_KEY] = pool


async def destroy_database_pool(app: Application) -> None:
    pool: Pool = app[DB_KEY]
    await pool.close()
