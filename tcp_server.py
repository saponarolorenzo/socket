import socket

HOST = "127.0.0.1"
PORT = 5000
BUFFER_SIZE = 1024


def create_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((HOST, PORT))
    server.listen()
    return server


def handle_client(conn, addr):
    print(f"[TCP SERVER] Connected by {addr}")

    while True:
        data = conn.recv(BUFFER_SIZE)

        if not data:
            print("[TCP SERVER] Client disconnected")
            break

        message = data.decode()

        print(f"[TCP SERVER] Received: {message}")

        if message == "PING":
            conn.sendall(b"PONG")


def main():
    with create_server() as server:
        print(f"[TCP SERVER] Listening on {HOST}:{PORT}")

        conn, addr = server.accept()

        with conn:
            handle_client(conn, addr)


if __name__ == "__main__":
    main()