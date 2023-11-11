"""
Чтение данных из сокета
"""
import socket

BUFFER_SIZE = 2  # bytes

# Create TCP server:
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

server_address = ("127.0.0.1", 8000)
server_socket.bind(server_address)
server_socket.listen()

try:
    connection, client_address = server_socket.accept()
    print(f"client_address = {client_address}")

    buffer = b""

    while buffer[-2:] != b"\r\n":
        data = connection.recv(BUFFER_SIZE)
        if not data:
            break
        else:
            print(f"Received data: '{data}'")
            buffer += data
    print(f"Full data: '{buffer}'")
    connection.sendall(buffer)
finally:
    server_socket.close()
