from pysnmp.hlapi import *

# Определяем адрес и параметры SNMP агента
agent_address = '192.168.0.1'
community_string = 'public'

# Определяем OID, который будет использоваться для получения информации о загрузке процессора
cpu_load_oid = '1.3.6.1.4.1.12345.1.1.0'

# Отправляем запрос к SNMP агенту
error_indication, error_status, error_index, var_binds = next(
    getCmd(SnmpEngine(),
           CommunityData(community_string),
           UdpTransportTarget((agent_address, 161)),
           ContextData(),
           ObjectType(ObjectIdentity(cpu_load_oid)))
)

# Обрабатываем полученные данные
if error_indication:
    print('Ошибка: %s' % error_indication)
else:
    if error_status:
        print('Ошибка: %s at %s' % (error_status.prettyPrint(), error_index and var_binds[int(error_index) - 1][0] or '?'))
    else:
        for var_bind in var_binds:
            print(' = '.join([x.prettyPrint() for x in var_bind]))