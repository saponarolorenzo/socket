import socket
import time

HOST = "127.0.0.1"
PORT = 5001
BUFFER_SIZE = 1024

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as client:

    for i in range(5):
        client.sendto(b"PING", (HOST, PORT))

        data, _ = client.recvfrom(BUFFER_SIZE)

        print(f"[CLIENT] Received: {data.decode()}")

        time.sleep(1)