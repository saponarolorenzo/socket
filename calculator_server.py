"""
PROTOCOL DESIGN

Protocol:
- TCP
- Reliable communication is required because calculations
  should not be lost.

Message format:
- Plain text arithmetic expressions
- Example:
    2 + 3

Malformed messages:
- Server returns "ERROR"

Termination:
- Client sends QUIT
- Client initiates termination
"""

import socket

HOST = "127.0.0.1"
PORT = 6000
BUFFER_SIZE = 1024


def evaluate_expression(expression):
    try:
        result = eval(expression)
        return str(result)

    except:
        return "ERROR"


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:

    server.bind((HOST, PORT))
    server.listen()

    print("[SERVER] Calculator server running")

    conn, addr = server.accept()

    with conn:
        print(f"[SERVER] Connected: {addr}")

        while True:
            data = conn.recv(BUFFER_SIZE)

            if not data:
                break

            message = data.decode()

            if message == "QUIT":
                break

            result = evaluate_expression(message)

            conn.sendall(result.encode())

    print("[SERVER] Connection closed")