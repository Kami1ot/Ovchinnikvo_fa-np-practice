import socket
import json

# Загружаем базу данных клиентов из файла
try:
    with open('clients.json', 'r') as f:
        clients = json.load(f)
except (FileNotFoundError, json.JSONDecodeError):
    clients = {}

# Создаем сокет и привязываем его к порту
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('localhost', 9009))
s.listen(1)
print('Server is listening on port 9009')

# Принимаем соединения от клиентов и обрабатываем их
while True:
    conn, addr = s.accept()
    print('Client connected:', addr)

    # Преобразуем кортеж addr в строку
    addr_str = ':'.join(map(str, addr))

    # Проверяем, известен ли нам клиент
    if addr_str in clients:
        name = clients[addr_str]
        conn.sendall(f'Hello, {name}!'.encode())
    else:
        # Запрашиваем у клиента его имя
        conn.sendall(b'What is your name?')
        data = conn.recv(1024)
        name = data.decode().strip()

        # Добавляем клиента в базу данных
        clients[addr_str] = name
        with open('clients.json', 'w') as f:
            # Преобразуем ключи словаря clients в строки
            json.dump({str(k): v for k, v in clients.items()}, f)

        conn.sendall(f'Hello, {name}!'.encode())

    # Общаемся с клиентом
    while True:
        data = conn.recv(1024)
        if not data:
            break
        conn.sendall(data)

    conn.close()
