import socket
import time

HOST = "127.0.0.1"
PORT = 5001
BUFFER_SIZE = 1024
TIMEOUT = 2


with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as client:

    client.settimeout(TIMEOUT)

    for i in range(5):

        print(f"[CLIENT] Sending PING #{i + 1}")

        client.sendto(b"PING", (HOST, PORT))

        try:
            data, _ = client.recvfrom(BUFFER_SIZE)

            print(f"[CLIENT] Received: {data.decode()}")

        except socket.timeout:
            print("[CLIENT] Packet lost or server unreachable")

        time.sleep(1)