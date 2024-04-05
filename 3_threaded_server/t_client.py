import socket

def main():
    host = '127.0.0.1'
    port = 12345

    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((host, port))

    while True:
        data = input("Enter data: ")
        if not data:
            break
        client.sendall(data.encode())
        response = client.recv(1024).decode()
        print("Received:", response)

    client.close()

if __name__ == "__main__":
    main()
