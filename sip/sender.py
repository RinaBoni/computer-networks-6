import socket
import sip

# Создаем сокет
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Указываем адрес и порт отправителя
source_address = ('192.168.0.10', 5061)

# Указываем адрес и порт получателя
destination_address = ('192.168.0.14', 5060)

i = 0
while (True):

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
    
    i+=1
    
    if (i>5000):
        break

# Закрываем сокет
s.close()
