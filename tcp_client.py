import socket
import threading

HOST = "127.0.0.1"
PORT = 5000
BUFFER_SIZE = 1024


def handle_client(conn, addr):
    print(f"[THREAD] Client connected: {addr}")

    with conn:
        while True:
            data = conn.recv(BUFFER_SIZE)

            if not data:
                break

            if data.decode() == "PING":
                conn.sendall(b"PONG")

    print(f"[THREAD] Client disconnected: {addr}")


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
    server.bind((HOST, PORT))
    server.listen()

    print("[SERVER] Multi-threaded server running")

    while True:
        conn, addr = server.accept()

        thread = threading.Thread(
            target=handle_client,
            args=(conn, addr)
        )

        thread.start()