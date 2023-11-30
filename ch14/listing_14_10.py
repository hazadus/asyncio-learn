"""
Сокеты и будущие объекты
"""
import functools
import selectors
import socket
from selectors import BaseSelector

from listing_14_8 import CustomFuture


def accept_connection(future: CustomFuture, connection: socket):
    print(f"Request for connection from {connection}!")
    future.set_result(connection)


async def sock_accept(sel: BaseSelector, sock) -> socket:
    print("Registering socket to listen for connections.")
    future = CustomFuture()
    sel.register(
        sock, selectors.EVENT_READ, functools.partial(accept_connection, future)
    )
    print("Listening for connections...")
    connection: socket = await future
    return connection


async def main(sel: BaseSelector):
    sock = socket.socket()
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    sock.bind(("127.0.0.1", 8000))
    sock.listen()
    sock.setblocking(False)

    print("Waiting connections to socket!")
    connection = await sock_accept(sel, sock)
    print(f"Got connection {connection}!")


selector = selectors.DefaultSelector()
coro = main(selector)

while True:
    try:
        state = coro.send(None)
        events = selector.select()

        for key, mask in events:
            print("Processing selector events...")
            callback = key.data
            callback(key.fileobj)
    except StopIteration as si:
        print("App finished.")
        break
