"""
Создание подкласса `Thread` для чистой остановки
"""
import socket
from threading import Thread


class ClientEchoThread(Thread):
    def __init__(self, client):
        super().__init__()
        self.client = client

    def run(self):
        try:
            while True:
                data = self.client.recv(2048)
                # If there's no data, then the connection was closed:
                if not data:
                    raise BrokenPipeError("Connection was closed.")
                print(f"Received {data}, sending it back!")
                self.client.sendall(data)
        except OSError as ex:
            # OSError is raised when the clien socket is closed:
            print(f"Thread interrupted by exception '{ex}', stopping thread!")

    def close(self):
        if self.is_alive():
            self.client.sendall(bytes("Stopping!", encoding="utf-8"))
            # Shut down client connection, stopping read/write operations:
            self.client.shutdown(socket.SHUT_RDWR)


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server.bind(("127.0.0.1", 8000))
    server.listen()
    connection_threads = []

    try:
        while True:
            print("Waiting for new connection...")
            connection, address = server.accept()
            print("New connection from", address)
            thread = ClientEchoThread(connection)
            connection_threads.append(thread)
            print("Total connections:", len(connection_threads))
            thread.start()
    except KeyboardInterrupt:
        print("Stopping!")
        [thread.close() for thread in connection_threads]
