import socket

HOST = "127.0.0.1"
PORT = 5000
BUFFER_SIZE = 1024
MAX_CLIENTS = 3


def handle_client(conn, addr):
    print(f"[SERVER] Connected: {addr}")

    while True:
        data = conn.recv(BUFFER_SIZE)

        if not data:
            break

        if data.decode() == "PING":
            conn.sendall(b"PONG")

    print(f"[SERVER] Disconnected: {addr}")


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
    server.bind((HOST, PORT))
    server.listen()

    print("[SERVER] Waiting for clients...")

    served_clients = 0

    while served_clients < MAX_CLIENTS:
        conn, addr = server.accept()

        with conn:
            handle_client(conn, addr)

        served_clients += 1

    print("[SERVER] Shutdown")