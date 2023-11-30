"""
Сервер с контекстными переменными
"""
import asyncio
from asyncio import StreamReader, StreamWriter
from contextvars import ContextVar


class Server:
    user_address = ContextVar("user_address")

    def __init__(self, host: str, port: int):
        self.host = host
        self.port = port

    async def start_server(self):
        server = await asyncio.start_server(
            self._client_connected,
            self.host,
            self.port,
        )
        await server.serve_forever()

    def _client_connected(self, reader: StreamReader, writer: StreamWriter):
        self.user_address.set(writer.get_extra_info("peername"))
        asyncio.create_task(self.listen_for_messages(reader))

    async def listen_for_messages(self, reader: StreamReader):
        while data := await reader.readline():
            print(f"Received message {data} from {self.user_address.get()}")


async def main():
    server = Server("127.0.0.1", 9000)
    await server.start_server()


asyncio.run(main())
