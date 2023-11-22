"""
Оконечная точка `/brands` в приложении Starlette

Runnning the app:
uvicorn --workers 8 --log-level error ch9.listing_9_8:app

Load testing:
wrk -c200 -t1 -d30 http://127.0.0.1:8000/brands

Test results:
Running 30s test @ http://127.0.0.1:8000/brands
  1 threads and 200 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency    66.45ms   68.39ms 714.94ms   86.31%
    Req/Sec     3.89k   705.03     4.98k    70.67%
  116222 requests in 30.02s, 1.70GB read
Requests/sec:   3871.20
Transfer/sec:     57.84MB
"""
from typing import Dict, List

import asyncpg
from asyncpg import Record
from asyncpg.pool import Pool
from starlette.applications import Starlette
from starlette.requests import Request
from starlette.responses import JSONResponse, Response
from starlette.routing import Route

app: Starlette


async def create_database_pool() -> None:
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
    app.state.DB = pool


async def destroy_database_pool() -> None:
    print("Destroying DB connection pool.")
    pool: Pool = app.state.DB
    await pool.close()


async def brands(request: Request) -> Response:
    connection: Pool = request.app.state.DB
    brand_query = "SELECT brand_id, brand_name FROM brand"
    results: List[Record] = await connection.fetch(brand_query)
    # Convert Records to dicts, because aiohttp can't serialize Records to JSON:
    result_as_dict: List[Dict] = [dict(brand) for brand in results]
    return JSONResponse(result_as_dict)


app = Starlette(
    routes=[Route("/brands", brands)],
    on_startup=[create_database_pool],
    on_shutdown=[destroy_database_pool],
)
