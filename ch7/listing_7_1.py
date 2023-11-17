"""
Многопоточный эхо-сервер
"""
import socket
from threading import Thread


def echo(client: socket) -> None:
    while True:
        data = client.recv(2048)
        print(f"Received {data}, sending it back!")
        client.sendall(data)


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server.bind(("127.0.0.1", 8000))
    server.listen()

    while True:
        print("Waiting for new connection...")
        connection, _ = server.accept()
        print("Got connection:", connection)
        # Create new thread for each connection:
        thread = Thread(target=echo, args=(connection,))
        thread.daemon = True
        thread.start()
