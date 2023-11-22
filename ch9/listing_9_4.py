"""
Оконечная точка для создания товара

Test results:
(.venv) hazadus:19:47:Projects/ayncio-learn# wrk -c200 -t1 -d30 http://127.0.0.1:8080/brands

Running 30s test @ http://127.0.0.1:8080/brands
  1 threads and 200 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency    87.33ms   28.50ms 420.69ms   89.34%
    Req/Sec     2.31k    92.95     2.46k    87.33%
  68855 requests in 30.01s, 1.11GB read
Requests/sec:   2294.63
Transfer/sec:     37.92MB
"""
from aiohttp import web
from aiohttp.web_request import Request
from aiohttp.web_response import Response
from ch9.listing_9_2 import create_database_pool, destroy_database_pool


routes = web.RouteTableDef()
DB_KEY = "database"


@routes.post("/product")
async def create_product(request: Request) -> Response:
    PRODUCT_NAME = "product_name"
    BRAND_ID = "brand_id"

    if not request.can_read_body:
        raise web.HTTPBadRequest()

    body = await request.json()
    print(body)

    if PRODUCT_NAME in body and BRAND_ID in body:
        db = request.app[DB_KEY]
        await db.execute(
            """
            INSERT INTO product(product_id, product_name, brand_id) VALUES (DEFAULT, $1, $2)
            """,
            body[PRODUCT_NAME],
            int(body[BRAND_ID]),
        )
        return web.Response(status=201)
    else:
        raise web.HTTPBadRequest()


app = web.Application()
app.on_startup.append(create_database_pool)
app.on_cleanup.append(destroy_database_pool)

app.add_routes(routes)
web.run_app(app)
