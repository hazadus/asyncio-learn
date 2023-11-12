"""
Построение асинхронного эхо-сервера
"""
import asyncio
import logging
import socket
from asyncio import AbstractEventLoop

BUFFER_SIZE = 1024


async def echo(connection: socket, loop: AbstractEventLoop) -> None:
    """
    Wait for data from the client and send it back.
    """
    try:
        while data := await loop.sock_recv(connection, BUFFER_SIZE):
            print("Received data:", data)
            await loop.sock_sendall(connection, data)
    except Exception as ex:
        logging.exception(exc_info=ex)
    finally:
        connection.close()


tasks = []


async def listen_for_connection(server_socket: socket, loop: AbstractEventLoop) -> None:
    """
    Listen for connections, and create `echo` task for each connection.
    """
    while True:
        connection, address = await loop.sock_accept(server_socket)
        connection.setblocking(False)
        print(f"Connection from {address}")
        tasks.append(asyncio.create_task(echo(connection, loop)))


async def main() -> None:
    # Create TCP server:
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    server_address = ("127.0.0.1", 8000)
    server_socket.setblocking(False)  # Mark server socket as non-blocking
    server_socket.bind(server_address)
    server_socket.listen()

    await listen_for_connection(server_socket, asyncio.get_event_loop())


asyncio.run(main())
