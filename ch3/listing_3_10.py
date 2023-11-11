"""
Корректная остановка
"""
import asyncio
import logging
import socket
import signal
from asyncio import AbstractEventLoop
from typing import List


async def echo(connection: socket, _loop: AbstractEventLoop) -> None:
    try:
        while data := await _loop.sock_recv(connection, 1024):
            print("Received data!")
            if data == b"boom\r\n":
                raise Exception("Server go BOOM!")
            await _loop.sock_sendall(connection, data)
    except Exception as ex:
        logging.exception(exc_info=ex)
    finally:
        connection.close()


echo_tasks = []


async def connection_listener(server_socket: socket, loop: AbstractEventLoop) -> None:
    while True:
        connection, address = await loop.sock_accept(server_socket)
        connection.setblocking(False)
        print(f"Got connection from {address}")
        echo_task = asyncio.create_task(echo(connection, loop))
        echo_tasks.append(echo_task)


class GracefulExit(SystemExit):
    pass


def shutdown() -> None:
    raise GracefulExit()


async def close_echo_tasks(tasks: List[asyncio.Task]):
    waiters = [asyncio.wait_for(task, 2) for task in tasks]
    for task in waiters:
        try:
            await task
        except asyncio.exceptions.TimeoutError:
            pass


loop = asyncio.new_event_loop()


async def main():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    server_address = ("127.0.0.1", 8000)
    server_socket.setblocking(False)  # Mark server socket as non-blocking
    server_socket.bind(server_address)
    server_socket.listen()

    for signame in {"SIGINT", "SIGTERM"}:
        loop.add_signal_handler(getattr(signal, signame), shutdown)

    await connection_listener(server_socket, loop)


try:
    loop.run_until_complete(main())
except GracefulExit:
    loop.run_until_complete(close_echo_tasks(echo_tasks))
finally:
    loop.close()
