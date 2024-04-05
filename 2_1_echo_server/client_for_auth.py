import socket
from getpass import getpass

def main():
    host = '127.0.0.1'
    port = 12345

    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((host, port))

    while True:
        data = client.recv(1024).decode()
        print(data)
        if "enter your name" in data.lower():
            name = input("Enter your name: ")
            client.sendall(name.encode())
        elif "enter your password" in data.lower():
            password = getpass.getpass("Enter your password: ")
            client.sendall(password.encode())
        elif "welcome" in data.lower() or "hello" in data.lower():
            break

    client.close()

if __name__ == "__main__":
    main()
