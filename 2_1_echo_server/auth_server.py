import socket
import json
from getpass import getpass

def load_clients():
    try:
        with open('clients.json', 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return {}

def save_clients(clients):
    with open('clients.json', 'w') as f:
        json.dump(clients, f)

def handle_client(connection, address):
    clients = load_clients()
    if address[0] in clients:
        connection.sendall("Please enter your password:".encode())
        password = connection.recv(1024).decode().strip()
        if clients[address[0]]['password'] == password:
            connection.sendall(f"Hello, {clients[address[0]]['name']}!".encode())
        else:
            connection.sendall("Incorrect password.".encode())
    else:
        connection.sendall("Please enter your name:".encode())
        name = connection.recv(1024).decode().strip()
        connection.sendall("Please enter your password:".encode())
        password = connection.recv(1024).decode().strip()
        clients[address[0]] = {'name': name, 'password': password}
        save_clients(clients)
        connection.sendall(f"Welcome, {name}!".encode())
    connection.close()

def main():
    host = '127.0.0.1'
    port = 12345

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((host, port))
    server.listen(1)

    print("Server is listening on {}:{}".format(host, port))

    while True:
        connection, address = server.accept()
        print("Connected by", address)
        handle_client(connection, address)

if __name__ == "__main__":
    main()
