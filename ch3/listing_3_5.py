"""
Первая попытка создать неблокирующий сервер
"""
import socket

BUFFER_SIZE = 2  # bytes

# Create TCP server:
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

server_address = ("127.0.0.1", 8000)
server_socket.bind(server_address)
server_socket.listen()
server_socket.setblocking(False)  # Mark server socket as non-blocking

connections = []

try:
    while True:
        connection, client_address = server_socket.accept()
        connection.setblocking(False)  # Mark client socket as non-blocking
        print(f"client_address = {client_address}")
        connections.append(connection)

        for connection in connections:
            buffer = b""

            while buffer[-2:] != b"\r\n":
                data = connection.recv(BUFFER_SIZE)
                if not data:
                    break
                else:
                    print(f"Received data: '{data}'")
                    buffer += data
            print(f"Full data: {buffer}")
            connection.sendall(buffer)
finally:
    server_socket.close()