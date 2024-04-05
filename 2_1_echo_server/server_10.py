import socket
import logging
import threading

def handle_client(conn, addr):
    while True:
        data = conn.recv(1024)
        if not data:
            logger.info('Client disconnected:%s', addr)
            break
        conn.sendall(data)
    conn.close()

# Настройка логгера
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(message)s')
file_handler = logging.FileHandler('server.log')
file_handler.setLevel(logging.INFO)
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)

# Запрашиваем у пользователя номер порта
port = input('Enter port number (default: 9009): ')
if not port:
    port = 9009
else:
    try:
        port = int(port)
    except ValueError:
        print('Invalid port number. Using default port 9009.')
        port = 9009

# Создаем сокет и привязываем его к порту
while True:
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.bind(('localhost', port))
        s.listen(2)
        logger.info('Server is listening on port %s', port)
        print('Server is listening on port', port)
        break
    except OSError:
        port += 1
        logger.info('Port %s is busy, trying port %s...', port-1, port)

# Принимаем соединения от клиентов и обрабатываем их в отдельных потоках
while True:
    conn, addr = s.accept()
    logger.info('Client connected: %s', addr)
    client_thread = threading.Thread(target=handle_client, args=(conn, addr))
    client_thread.start()

# Обработка клиентов

