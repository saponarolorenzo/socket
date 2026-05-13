import socket
import time

HOST = "127.0.0.1"
PORT = 5001
BUFFER_SIZE = 1024
PING_COUNT = 5
TIMEOUT = 2


def send_ping(sock, number):
    print(f"[UDP CLIENT] Sending PING #{number}")

    sock.sendto(b"PING", (HOST, PORT))

    try:
        data, _ = sock.recvfrom(BUFFER_SIZE)
        print(f"[UDP CLIENT] Received: {data.decode()}")

    except socket.timeout:
        print("[UDP CLIENT] Timeout waiting for response")


def main():
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as client:
        client.settimeout(TIMEOUT)

        for i in range(1, PING_COUNT + 1):
            send_ping(client, i)
            time.sleep(1)


if __name__ == "__main__":
    main()