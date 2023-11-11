"""
Использование селектора для построения неблокирующего сервера
"""
import selectors
import socket
from selectors import SelectorKey
from typing import List, Tuple

BUFFER_SIZE = 1024  # bytes

selector = selectors.DefaultSelector()

# Create TCP server:
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

server_address = ("127.0.0.1", 8000)
server_socket.bind(server_address)
server_socket.listen()
server_socket.setblocking(False)  # Mark server socket as non-blocking

selector.register(server_socket, selectors.EVENT_READ)

while True:
    events: List[Tuple[SelectorKey, int]] = selector.select(timeout=1)

    if len(events) == 0:
        print("No events yet.")

    for event, _ in events:
        # Socket where event happened:
        event_socket = event.fileobj

        if event_socket == server_socket:
            # If event happened with server socket, it means there's a connection:
            connection, client_address = server_socket.accept()
            connection.setblocking(False)  # Mark client socket as non-blocking
            print(f"Connection from {client_address}")
            selector.register(connection, selectors.EVENT_READ)
        else:
            data = event_socket.recv(BUFFER_SIZE)
            print(f"Received data: {data}")
            event_socket.send(data)
