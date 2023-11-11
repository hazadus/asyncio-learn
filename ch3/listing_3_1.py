"""
Запуск сервера и прослушивание порта для подключения

telnet 127.0.0.1 8000
"""
import socket

# Create TCP server:
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

server_address = ("127.0.0.1", 8000)
server_socket.bind(server_address)
server_socket.listen()

connection, client_address = server_socket.accept()
print(f"connection = {connection}; client_address = {client_address}")
print(f"client_address = {client_address}")
