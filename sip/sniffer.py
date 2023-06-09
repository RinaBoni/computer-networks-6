import socket
import sip
import pandas as pd
from scapy.all import *

UDP_MAX_SIZE = 65535  # максимальный размер udp пакета

host = socket.gethostbyname((socket.gethostname()))
port = 5060

def to_cvs (type_of_packet, message):
    # df = pd.DataFrame({'Type': 'SIP '[type_of_packet], 'Message': [message]})
    df = pd.DataFrame({'Type': ["SIP", ""][type_of_packet], 'Message': [message]})
    # Записываем DataFrame в файл CSV
    df.to_csv('packets.csv', mode='a', header=False, index=False)
    print('занес')

def to_dataframe(msg):
    """заносим все в датафрейм и в csv файл"""
    #заносим все в датафрейм
    df = pd.DataFrame(msg)
    #создаем файл csv
    filename = 'packets.csv'
    #заносим датафрейм в csv файл
    df.to_csv(filename)

    

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
        
        
        # Открываем файл для записи
        file = open('sip.txt', 'w')
        
        msg = message.decode()

        if (msg == sip.message_BYE or msg == sip.message_ACK or msg == sip.message_CANCEL or msg == sip.message_INFO or msg == sip.message_INVITE or msg == sip.message_MESSAGE or msg == sip.message_NOTIFY or msg == sip.message_OPTIONS or msg == sip.message_PRACK or msg == sip.message_PUBLISH or msg == sip.message_REFER or msg == sip.message_REGISTER or msg == sip.message_UPDATE or msg == sip.message_SUBSCRIBE):
            # to_dataframe(msg)
            df = pd.DataFrame({'Message': [msg]})
            df.to_csv('packets.csv', mode='a', header=False, index=False)
            
            
        # Закрываем файл
        file.close()
        
    
    # # Создаем DataFrame с информацией о пакете
    #         df = pd.DataFrame({'Type': 'SIP BYE', 'Message': [msg]})

    #         # Записываем DataFrame в файл CSV
    #         df.to_csv('packets.csv', mode='a', header=False, index=False)
    #         # to_cvs('BYE', msg)
    # members = []
    # while True:
    #     message, addr = s.recvfrom(UDP_MAX_SIZE)        # Слушаем порт. Адрес откуда пришел пакет
    #     print(f'reciv msg:z{message}')
    #     # Проверяем есть ли клиент в списке участников
    #     if addr not in members:
    #         members.append(addr)

    #     # Если сообщение пустое ничего не делаем
    #     if not message:
    #         continue

    #     # ID клиента это его порт
    #     client_id = addr[1]
    #     # Говорим серверу, что клиент присоединился к чату, чтобы мы могли уведомить его о новом сообщении
    #     if message.decode('ascii') == '__join':
    #         print(f'Client {client_id} joined chat')
    #         continue

    #     # Отправляем уведомление об сообщении всем кроме отправителя
    #     message = f'client {client_id}: {message.decode("ascii")}'
    #     for member in members:
    #         if member == addr:
    #             continue
    #         s.sendto(message.encode('ascii'), member)


if __name__ == '__main__':
    listen(host, port)





# def filter():
    
#     f = open('test-template.txt')
#     file_request = f.read()
#     f.close()
#     print(file_request)


# def sniff(interface):
#     # filter_str = "udp and port 5061 and (udp[8]==0x53)"
#     filter_str = filter()
#     print ('пакет1')
#     scapy.sniff(iface=interface, filter=filter_str, store=False, prn=process_sniffed_packet)
#     print ('пакет2')

# def process_sniffed_packet(packet):
#     print(packet.show())
#     print ('пакет3')


# sniff('Ethernet')



