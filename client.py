import socket

HOST = "   "  # The server's hostname or IP address
PORT = _____  # The port used by the server

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.sendall(b"THIS IS FIRST SOCKET PROGRAM")
    data = s.recv(1024)

print("Received", repr(data))