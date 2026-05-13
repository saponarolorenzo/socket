import socket

HOST = "127.0.0.1"
PORT = 5001
BUFFER_SIZE = 1024


def create_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server.bind((HOST, PORT))
    return server


def main():
    with create_server() as server:
        print(f"[UDP SERVER] Listening on {HOST}:{PORT}")

        while True:
            data, addr = server.recvfrom(BUFFER_SIZE)

            message = data.decode()

            print(f"[UDP SERVER] Received from {addr}: {message}")

            if message == "PING":
                server.sendto(b"PONG", addr)


if __name__ == "__main__":
    main()