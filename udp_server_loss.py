import socket
import random

HOST = "127.0.0.1"
PORT = 5001
BUFFER_SIZE = 1024
DROP_PROBABILITY = 0.3


with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as server:
    server.bind((HOST, PORT))

    print("[SERVER] UDP unreliable server running")

    while True:
        data, addr = server.recvfrom(BUFFER_SIZE)

        message = data.decode()

        print(f"[SERVER] Received: {message}")

        if random.random() < DROP_PROBABILITY:
            print("[SERVER] Dropped reply (simulated loss)")
            continue

        server.sendto(b"PONG", addr)