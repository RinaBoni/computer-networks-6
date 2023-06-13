import socket
import sip
import random_packets


host = socket.gethostbyname((socket.gethostname()))
port = 5061

# Создаем сокет
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Указываем адрес и порт отправителя
source_address = (socket.gethostbyname((socket.gethostname())), 5061)
s.bind((host, port))

# Указываем адрес и порт получателя
destination_address = (socket.gethostbyname((socket.gethostname())), 5060)
print(f'Senging from: {source_address} to: {destination_address}')

i = 0
while (i<10):

    # Отправляем пакет на получателя
    s.sendto(sip.message_INVITE.encode(), destination_address)
    s.sendto(sip.message_REGISTER.encode(), destination_address)
    s.sendto(sip.message_ACK.encode(), destination_address)
    s.sendto(sip.message_BYE.encode(), destination_address)
    s.sendto(sip.message_UPDATE.encode(), destination_address)
    s.sendto(sip.message_REFER.encode(), destination_address)
    s.sendto(sip.message_PRACK.encode(), destination_address)
    s.sendto(sip.message_NOTIFY.encode(), destination_address)
    s.sendto(sip.message_SUBSCRIBE.encode(), destination_address)
    s.sendto(sip.message_PUBLISH.encode(), destination_address)
    s.sendto(sip.message_MESSAGE.encode(), destination_address)
    s.sendto(sip.message_INFO.encode(), destination_address)
    s.sendto(sip.message_OPTIONS.encode(), destination_address)
    s.sendto(random_packets.message_NOhgfdsTIFY.encode(), destination_address)
    s.sendto(random_packets.message_NOTIkjhgfjhgFY.encode(), destination_address)

    i+=1
    
#     if (i>5):
#         break
    
# Отправляем пакет на получателя
# s.sendto(sip.message_INVITE.encode(), destination_address)
# s.sendto(sip.message_REGISTER.encode(), destination_address)
# s.sendto(sip.message_ACK.encode(), destination_address)
# s.sendto(sip.message_BYE.encode(), destination_address)
# s.sendto(sip.message_UPDATE.encode(), destination_address)
# s.sendto(sip.message_REFER.encode(), destination_address)
# s.sendto(sip.message_PRACK.encode(), destination_address)
# s.sendto(sip.message_NOTIFY.encode(), destination_address)
# s.sendto(sip.message_SUBSCRIBE.encode(), destination_address)
# s.sendto(sip.message_PUBLISH.encode(), destination_address)
# s.sendto(sip.message_MESSAGE.encode(), destination_address)
# s.sendto(sip.message_INFO.encode(), destination_address)
# s.sendto(sip.message_OPTIONS.encode(), destination_address)

# Закрываем сокет
s.close()
