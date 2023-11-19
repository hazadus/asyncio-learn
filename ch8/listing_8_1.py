"""
Выполнение HTTP-запроса с помощью транспортного механизма и протокола
"""
import asyncio
from asyncio import AbstractEventLoop, Future, Transport
from typing import Optional


class HTTPGetClientProtocol(asyncio.Protocol):
    def __init__(self, host: str, loop: AbstractEventLoop):
        self._host: str = host
        self._future: Future = loop.create_future()
        self._transport: Optional[Transport] = None
        self._response_buffer: bytes = b""

    async def get_response(self):
        # await until we get response from the server:
        return await self._future

    def _get_request_bytes(self) -> bytes:
        request = (
            f"GET / HTTP/1.1\r\n" f"Connection: close\r\n" f"Host: {self._host}\r\n\r\n"
        )
        return request.encode()

    def connection_made(self, transport: Transport) -> None:
        print(f"Got connection to {self._host}")
        self._transport = transport
        # When connection is established, use transport to send request:
        self._transport.write(self._get_request_bytes())

    def data_received(self, data):
        print("Data received!")
        # Store received data in internal buffer
        self._response_buffer += data

    def eof_received(self) -> Optional[bool]:
        self._future.set_result(self._response_buffer.decode())
        return False

    def connection_lost(self, exc: Optional[Exception]) -> None:
        if exc is None:
            print("Connection closed without errors.")
        else:
            self._future.set_exception(exc)
