"""
Оконечная точка типа WebSocket в Starlette

Running the app:
uvicorn --workers 1 ch9.listing_9_9:app

Отметим, что в данном примере рабочий процесстолько один, поскольку мы
храним в памяти разделяемое состояние (список сокетов); если бы рабочих
процессов было несколько, то у каждого был бы свой список сокетов.
В таком случае нужно было бы использовать какое-то постоянное хранилище,
например базу данных.
"""
import asyncio
import typing
from typing import List

from starlette.applications import Starlette
from starlette.endpoints import WebSocketEndpoint
from starlette.routing import WebSocketRoute
from starlette.websockets import WebSocket


class UserCounter(WebSocketEndpoint):
    encoding = "text"
    sockets: List[WebSocket] = []

    async def on_connect(self, websocket: WebSocket) -> None:
        await websocket.accept()
        UserCounter.sockets.append(websocket)
        await self._send_count()

    async def on_disconnect(self, websocket: WebSocket, close_code: int) -> None:
        UserCounter.sockets.remove(websocket)
        await self._send_count()

    async def on_receive(self, websocket: WebSocket, data: typing.Any) -> None:
        ...

    async def _send_count(self) -> None:
        if len(UserCounter.sockets):
            count_str = str(len(UserCounter.sockets))
            task_to_socket = {
                asyncio.create_task(websocket.send_text(count_str)): websocket
                for websocket in UserCounter.sockets
            }

            done, pending = await asyncio.wait(task_to_socket)

            for task in done:
                if task.exception() is not None:
                    if task_to_socket[task] in UserCounter.sockets:
                        UserCounter.sockets.remove(task_to_socket[task])


app = Starlette(
    routes=[
        WebSocketRoute("/counter", UserCounter),
    ]
)
