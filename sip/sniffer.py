import socket
import sip
import pandas as pd
from scapy.all import *

UDP_MAX_SIZE = 65535  # максимальный размер udp пакета

host = socket.gethostbyname((socket.gethostname()))
port = 5060


def listen(host, port):
    """Функция для запуска сервера. На вход принимает адрес сервера и порт"""
    # Создаем сокет.
    # Первый параметр указывает на то, какое адресное пространство будет использовать (IPv4).
    # Второй параметр указывает на используемый протокол (UDP)
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # Привязываем к сокету адрес и хост
    s.bind((host, port))
    print(f'Listening at {host}:{port}')


    # Сервер в бесконечном цикле слушает клиентов и отправляет уведомления о сообщениях
    while (True):
        message, addr = s.recvfrom(UDP_MAX_SIZE)
        
        msg = message.decode()

        if (msg == sip.message_BYE or msg == sip.message_ACK or msg == sip.message_CANCEL or msg == sip.message_INFO or msg == sip.message_INVITE or msg == sip.message_MESSAGE or msg == sip.message_NOTIFY or msg == sip.message_OPTIONS or msg == sip.message_PRACK or msg == sip.message_PUBLISH or msg == sip.message_REFER or msg == sip.message_REGISTER or msg == sip.message_UPDATE or msg == sip.message_SUBSCRIBE):
            
            df = pd.DataFrame({'Message': [msg]})
            df.to_csv('packets.csv', mode='a', header=False, index=False)
            print(msg)
            

if __name__ == '__main__':
    listen(host, port)