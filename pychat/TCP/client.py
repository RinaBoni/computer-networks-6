import socket
import threading
import os

# Спрашиваем ник
nickname = input("Enter your nickname : ").strip()
# Убеждаемся что клиент ввел ник
while not nickname:
    nickname = input("Your nickname should not be empty : ").strip()

# Создаем сокет.
# Первый параметр указывает на то, какое адресное пространство будет использовать (IPv4).
# Второй параметр указывает на используемый протокол (TCP)
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Адрес хоста
host = "localhost"  # "127.0.1.1"
port = 8000
# Подключаемся к серверу
s.connect((host, port))


def thread_sending():
    """Отправка"""
    while True:
        # Записываем полученное сообщение
        message_to_send = input(f'{nickname}: ')
        # Если сообщение не пустое соединяем его с ником и отправляем на сервер
        if message_to_send:
            message_with_nickname = nickname + " : " + message_to_send
            s.send(message_with_nickname.encode())


def thread_receiving():
    """Прослушивание"""
    while True:
        message = s.recv(1024).decode()
        print('\r\r' + message + '\n' + f'{nickname}: ', end='')


# При запуске клиента автоматически очищается окно терминала и выводится приветствие
if __name__ == '__main__':
    os.system('cls')
    print('Welcome to chat!')
    # Создем два потока, по одному для каждой функции, и запускаем их
    thread_send = threading.Thread(target=thread_sending)
    thread_receive = threading.Thread(target=thread_receiving)
    thread_send.start()
    thread_receive.start()