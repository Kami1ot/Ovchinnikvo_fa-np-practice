import socket

# Запрашиваем у пользователя имя хоста и номер порта
host = input('Enter host name (default: localhost): ')
if not host:
    host = 'localhost'
port = input('Enter port number (default: 9009): ')
if not port:
    port = 9009
else:
    try:
        port = int(port)
    except ValueError:
        print('Invalid port number. Using default port 9009.')
        port = 9009

# Создаем сокет и подключаемся к серверу
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))
print('Client connected to {}:{}'.format(host, port))

# Отправляем сообщения серверу и получаем ответ
while True:
    user_input = input()
    if user_input == 'exit':
        break
    s.sendall(user_input.encode())
    data = s.recv(1024)
    if not data:
        break
    print("Data received from server: ", data.decode('utf-8'))

# Закрываем соединение
s.close()
print('Client disconnected.')
