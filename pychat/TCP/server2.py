import socket


def listen(host: str = socket.gethostbyname((socket.gethostname())), port: int = 3000):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((host, port))
    print(f'Listening at {host}:{port}')
    members = []
    while True:
        s.listen()
        client, client_address = s.accept()
        if client_address not in members:
            members.append(client_address)

        client_id = client_address[1]

        message = client.recv(1024).decode()

        if message.decode('ascii') == '__join':
            print(f'Client {client_id} joined chat')
            continue

        message = f'client {client_id}: {message.decode("ascii")}'
        for member in members:
            if member == client_address:
                continue
            member.send(message.encode())


if __name__ == '__main__':
    listen()
