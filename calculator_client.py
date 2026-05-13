"""
PROTOCOL DESIGN

Protocol:
- TCP

Message format:
- Plain text arithmetic expressions

Malformed messages:
- Server replies with ERROR

Termination:
- Client sends QUIT
"""

import socket

HOST = "127.0.0.1"
PORT = 6000
BUFFER_SIZE = 1024


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:

    client.connect((HOST, PORT))

    while True:

        expression = input("Enter expression (or QUIT): ")

        client.sendall(expression.encode())

        if expression == "QUIT":
            break

        result = client.recv(BUFFER_SIZE)

        print("Result:", result.decode())