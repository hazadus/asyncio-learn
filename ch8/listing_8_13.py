"""
Чат-сервер
"""
import asyncio
import logging
from asyncio import StreamReader, StreamWriter


class ChatServer:
    def __init__(self):
        self._username_to_writer = {}

    async def start_chat_server(self, host: str, port: int) -> None:
        server = await asyncio.start_server(self.client_connected, host, port)

        async with server:
            await server.serve_forever()

    async def client_connected(
        self, reader: StreamReader, writer: StreamWriter
    ) -> None:
        print(f"CONNECTED {reader} {writer}")

        command = await reader.readline()
        command, args = command.split(b" ")

        if command == b"CONNECT":
            username = args.replace(b"\n", b"").decode()
            self._add_user(username, reader, writer)
            await self._on_connect(username, writer)
        else:
            logging.error("Received unsupported command from client, disconnecting.")
            writer.close()
            await writer.wait_closed()

    def _add_user(
        self, username: str, reader: StreamReader, writer: StreamWriter
    ) -> None:
        self._username_to_writer[username] = writer
        asyncio.create_task(self._listen_for_messages(username, reader))

    async def _on_connect(self, username: str, writer: StreamWriter) -> None:
        writer.write(
            f"Welcome! Users connected: {len(self._username_to_writer)}!\n".encode()
        )
        await writer.drain()
        await self._notify_all(f"{username} connected!\n")

    async def _remove_user(self, username: str) -> None:
        writer = self._username_to_writer[username]
        del self._username_to_writer[username]
        try:
            writer.close()
            await writer.wait_closed()
        except Exception as ex:
            logging.exception("Error during closing of client writer.", exc_info=ex)

    async def _listen_for_messages(self, username: str, reader: StreamReader) -> None:
        try:
            while (data := await asyncio.wait_for(reader.readline(), 60)) != b"":
                await self._notify_all(f"{username}: {data.decode()}")
            await self._notify_all(f"{username} has left the chat\n")
        except Exception as ex:
            logging.exception("Error reading data from client.", exc_info=ex)
            await self._remove_user(username)

    async def _notify_all(self, message: str) -> None:
        inactive_users = []

        for username, writer in self._username_to_writer.items():
            try:
                writer.write(message.encode())
                await writer.drain()
            except ConnectionError as ex:
                logging.exception("Error writing data to client.", exc_info=ex)
                inactive_users.append(username)

        [await self._remove_user(username) for username in inactive_users]


async def main() -> None:
    chat_server = ChatServer()
    await chat_server.start_chat_server("127.0.0.1", 8000)


asyncio.run(main())
