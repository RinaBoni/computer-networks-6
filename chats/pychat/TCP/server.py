import os
import socket
import threading

# Создаем сокет.
# Первый параметр указывает на то, какое адресное пространство будет использовать (IPv4).
# Второй параметр указывает на используемый протокол (TCP)
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Порт
PORT = 8000
# Пока что сообщаем адрес "0.0.0.0", поскольку не знаем, каким будет адрес клиента.
ADDRESS = "0.0.0.0"
# Список клиентов
broadcast_list = []
# Привязываем к сокету адрес и хост
s.bind((ADDRESS, PORT))
os.system('cls')
print(f'TCP server is running')


def accept_loop():
    """Обрабатываем соединение"""
    while True:
        # Запускаем режим прослушивания
        s.listen()
        # Говорим хосту принять клиента (входящее сообщение)
        client, client_address = s.accept()
        # Добавляем клиента в список
        broadcast_list.append(client)
        client_id = client_address[1]
        # Говорим серверу, что клиент присоединился к чату
        print(f'Client {client_id} joined chat')
        # Слушаем клиента
        start_listening_thread(client)


def start_listening_thread(client):
    """Создаем выделенный поток для этого клиента, который будет прослушивать сообщения и транслировать их"""
    client_thread = threading.Thread(
        target=listen_thread,
        args=(client,)  # Аргумент, который мы отправляем при вызове функции
    )
    client_thread.start()


def listen_thread(client):
    """Прослушиваем сообщения и транслируем их"""
    while True:
        message = client.recv(1024).decode()
        # Смотрим какое сообщение получили

        if message:
            print(f"Received message : {message}")
            # Отправляем сообщение всем участникам чата
            broadcast(message, client)
        # Если сообщение пустое, клиент отключился
        else:
            print(f"client has been disconnected : {client}")
            return


def broadcast(message, client):
    """Отправляем сообщение каждому клиенту в списке рассылки"""
    for cl in broadcast_list:
        try:
            if client == cl:
                continue
            cl.send(message.encode())
        except:
            broadcast_list.remove(client)
            print(f"Client removed : {client}")


accept_loop()
