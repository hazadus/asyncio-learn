"""
Подключение к базе данных о товарах
"""
from typing import Dict, List

import asyncpg
from aiohttp import web
from aiohttp.web_app import Application
from aiohttp.web_request import Request
from aiohttp.web_response import Response
from asyncpg import Record
from asyncpg.pool import Pool

routes = web.RouteTableDef()
DB_KEY = "database"


async def create_database_pool(app: Application) -> None:
    print("Creating DB connection pool.")
    pool: Pool = await asyncpg.create_pool(
        host="127.0.0.1",
        port=5432,
        user="postgres",
        password="postgres",
        database="products",
        min_size=6,
        max_size=6,
    )
    app[DB_KEY] = pool


async def destroy_database_pool(app: Application) -> None:
    print("Destroying DB connection pool.")
    pool: Pool = app[DB_KEY]
    await pool.close()


@routes.get("/brands")
async def brands(request: Request) -> Response:
    connection: Pool = request.app[DB_KEY]
    brand_query = "SELECT brand_id, brand_name FROM brand"
    results: List[Record] = await connection.fetch(brand_query)
    # Convert Records to dicts, because aiohttp can't serialize Records to JSON:
    result_as_dict: List[Dict] = [dict(brand) for brand in results]
    return web.json_response(result_as_dict)


app = web.Application()
app.on_startup.append(create_database_pool)
app.on_cleanup.append(destroy_database_pool)

app.add_routes(routes)
web.run_app(app)
