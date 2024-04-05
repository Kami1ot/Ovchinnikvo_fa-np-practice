import socket
import threading

def handle_client(connection, address):
    while True:
        data = connection.recv(1024)
        if not data:
            break
        connection.sendall(data)
    connection.close()

def main():
    host = '127.0.0.1'
    port = 12345

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((host, port))
    server.listen()

    print("Server is listening on {}:{}".format(host, port))

    while True:
        connection, address = server.accept()
        print("Connected by", address)
        client_thread = threading.Thread(target=handle_client, args=(connection, address))
        client_thread.start()

if __name__ == "__main__":
    main()
