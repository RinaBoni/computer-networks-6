import socket
import threading
import os

def listen(s: socket.socket):
    """Бесконечно слушает. Если получаем сообщение, то выводим его"""
    while True:
        message = s.recv(1024).decode()
        print('\r\r' + message + '\n' + f'you: ', end='')


def connect(host: str = socket.gethostbyname((socket.gethostname())), port: int = 3000):
    """Реализует все поведение клиента"""
    # Создаем сокет.
    # Первый параметр указывает на то, какое адресное пространство будет использовать (IPv4).
    # Второй параметр указывает на используемый протокол (UDP)
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # Подключаемся к серверу
    s.connect((host, port))

    # Слушаем чат в фоне
    threading.Thread(target=listen, args=(s,), daemon=True).start()

    # Сообщаем серверу, что подключились
    s.send('__join'.encode('ascii'))

    # Даем пользователю бесконечно писать в чат
    while True:
        message = input(f'you: ')
        s.send(message.encode('ascii'))

# При запуске клиента автоматически очищается окно терминала и выводится приветствие
if __name__ == '__main__':
    os.system('cls')
    print('Welcome to chat!')
    connect()