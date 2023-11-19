"""
Создание эхо-сервера с помощью серверных объектов
"""
import asyncio
import logging
from asyncio import StreamReader, StreamWriter


class ServerState:
    def __init__(self):
        self._writers = []

    async def add_client(self, reader: StreamReader, writer: StreamWriter) -> None:
        self._writers.append(writer)
        await self._on_connect(writer)
        asyncio.create_task(self._echo(reader, writer))

    async def _on_connect(self, writer: StreamWriter) -> None:
        writer.write(f"Welcome! Users online: {len(self._writers)}!\n".encode())
        await writer.drain()
        await self._notify_all("New user connected!\n")

    async def _echo(self, reader: StreamReader, writer: StreamWriter) -> None:
        try:
            while (data := await reader.readline()) != b"":
                writer.write(data)
                await writer.drain()
            self._writers.remove(writer)
            await self._notify_all(
                f"Client disconnected. Users left online: {len(self._writers)}!\n"
            )
        except Exception as ex:
            logging.exception("Error reading data from client.", exc_info=ex)
            self._writers.remove(writer)

    async def _notify_all(self, message: str) -> None:
        for writer in self._writers:
            try:
                writer.write(message.encode())
                await writer.drain()
            except ConnectionError as ex:
                logging.exception("Error sending data to client.", exc_info=ex)
                self._writers.remove(writer)


async def main() -> None:
    server_state = ServerState()

    async def client_connected(reader: StreamReader, writer: StreamWriter) -> None:
        await server_state.add_client(reader, writer)

    server = await asyncio.start_server(client_connected, "127.0.0.1", 8000)

    async with server:
        await server.serve_forever()


asyncio.run(main())
