"""
Использование очередей в веб-приложении
"""
import asyncio
from asyncio import Queue, Task
from random import randrange

from aiohttp import web
from aiohttp.web_app import Application
from aiohttp.web_request import Request
from aiohttp.web_response import Response

routes = web.RouteTableDef()

QUEUE_KEY = "order_queue"
TASKS_KEY = "order_tasks"

app = Application()


async def process_order_worker(worker_id: int, queue: Queue):
    while True:
        print(f"Worker {worker_id}: waiting for order...")
        order = await queue.get()
        print(f"Worker {worker_id}: processing order {order}.")
        await asyncio.sleep(order)
        print(f"Worker {worker_id}: order {order} processed!")
        queue.task_done()


@routes.post("/order")
async def place_order(request: Request) -> Response:
    order_queue = app[QUEUE_KEY]
    await order_queue.put(randrange(5))
    return Response(body="Order placed!")


async def create_order_queue(app: Application):
    print("Creating order and task queue...")
    queue = Queue(10)
    app[QUEUE_KEY] = queue
    app[TASKS_KEY] = [
        asyncio.create_task(process_order_worker(i, queue)) for i in range(5)
    ]


async def destroy_queue(app: Application):
    order_tasks: list[Task] = app[TASKS_KEY]
    queue: Queue = app[QUEUE_KEY]
    print("Waiting to stop workers...")
    try:
        await asyncio.wait_for(queue.join(), timeout=10)
    finally:
        print("Stopped order processing, now cancelling worker tasks...")
        [task.cancel() for task in order_tasks]


app.on_startup.append(create_order_queue)
app.on_cleanup.append(destroy_queue)

app.add_routes(routes)
web.run_app(app)
