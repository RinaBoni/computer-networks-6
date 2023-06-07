import socket

UDP_MAX_SIZE = 65535  # максимальный размер udp пакета


def listen(host: str = socket.gethostbyname((socket.gethostname())), port: int = 3000):
    """Функция для запуска сервера. На вход принимает адрес сервера и порт"""
    # Создаем сокет.
    # Первый параметр указывает на то, какое адресное пространство будет использовать (IPv4).
    # Второй параметр указывает на используемый протокол (UDP)
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # Привязываем к сокету адрес и хост
    s.bind((host, port))
    print(f'Listening at {host}:{port}')

    # Сервер в бесконечном цикле слушает клиентов и отправляет уведомления о сообщениях
    members = []
    while True:
        message, addr = s.recvfrom(UDP_MAX_SIZE)        # Слушаем порт. Адрес откуда пришел пакет
        print(f'reciv msg:z{message}')
        # Проверяем есть ли клиент в списке участников
        if addr not in members:
            members.append(addr)

        # Если сообщение пустое ничего не делаем
        if not message:
            continue

        # ID клиента это его порт
        client_id = addr[1]
        # Говорим серверу, что клиент присоединился к чату, чтобы мы могли уведомить его о новом сообщении
        if message.decode('ascii') == '__join':
            print(f'Client {client_id} joined chat')
            continue

        # Отправляем уведомление об сообщении всем кроме отправителя
        message = f'client {client_id}: {message.decode("ascii")}'
        for member in members:
            if member == addr:
                continue
            s.sendto(message.encode('ascii'), member)


if __name__ == '__main__':
    listen()
