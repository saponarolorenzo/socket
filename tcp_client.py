import socket
import time

HOST = "127.0.0.1"
PORT = 5000
BUFFER_SIZE = 1024
PING_COUNT = 5


def send_ping(sock, number):
    print(f"[TCP CLIENT] Sending PING #{number}")
    sock.sendall(b"PING")

    data = sock.recv(BUFFER_SIZE)

    print(f"[TCP CLIENT] Received: {data.decode()}")


def main():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
        client.connect((HOST, PORT))

        for i in range(1, PING_COUNT + 1):
            send_ping(client, i)
            time.sleep(1)


if __name__ == "__main__":
    main()