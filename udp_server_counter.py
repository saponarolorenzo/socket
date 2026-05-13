import socket

HOST = "127.0.0.1"
PORT = 5001
BUFFER_SIZE = 1024

counter = 0


with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as server:
    server.bind((HOST, PORT))

    print("[SERVER] UDP counter server running")

    while True:
        data, addr = server.recvfrom(BUFFER_SIZE)

        message = data.decode()

        if message == "PING":
            counter += 1

            response = f"PONG #{counter}"

            print(f"[SERVER] Sending: {response}")

            server.sendto(response.encode(), addr)