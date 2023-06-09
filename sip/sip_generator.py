from sipMessage import SIPMessage

# Создаем объект SIP-сообщения
sip_msg = SIPMessage()

# Устанавливаем заголовок (Header)
sip_msg.setMethod('INVITE')
sip_msg.setUri('sip:alice@example.com')
sip_msg.setVersion('SIP/2.0')

# Устанавливаем адреса (Addresses)
sip_msg.setFrom('sip:bob@example.com')
sip_msg.setTo('sip:alice@example.com')

# Устанавливаем тело сообщения (Message Body)
sip_msg.setBody('Hello, Alice!')

# Получаем текстовое представление SIP-сообщения
sip_msg_text = sip_msg.toString()

# Отправляем SIP-сообщение
send_sip_msg(sip_msg_text)