import socket
import json
import threading

# Загружаем базу данных клиентов из файла
try:
    with open('clients.json', 'r') as f:
        clients = json.load(f)
except (FileNotFoundError, json.JSONDecodeError):
    clients = {}

# Создаем сокет и привязываем его к порту
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('localhost', 9009))
s.listen(2)
print('Server is listening on port 9009')

# Функция для обработки клиентов
def handle_client(conn, addr):
    # Получаем имя клиента
    conn.sendall(b'What is your name?')
    data = conn.recv(1024)
    name = data.decode().strip()

    # Добавляем клиента в базу данных, если его там нет
    if addr not in clients:
        clients[addr] = name
        with open('clients.json', 'w') as f:
            json.dump(clients, f)

    # Приветствуем клиента по имени
    conn.sendall(f'Hello, {name}!'.encode())

    # Общаемся с клиентом
    while True:
        data = conn.recv(1024)
        if not data:
            break
        conn.sendall(data)

    conn.close()

# Принимаем соединения от клиентов и обрабатываем их в отдельных потоках
while True:
    conn, addr = s.accept()
    print('Client connected:', addr)
    client_thread = threading.Thread(target=handle_client, args=(conn, addr))
    client_thread.start()
