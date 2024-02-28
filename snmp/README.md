# Курсовая
##  Реализовать SNMP агент и менеджер для сбора сведений о программно-аппаратной части сетевых узлов

=======

[очень полезная информация](https://selectel.ru/blog/snmp/)

[Мониторинг сетей при помощи Python](http://onreader.mdl.ru/MasteringPythonNetworking/content/Ch07.html)

[документация к pysnmp](https://www.pysnmp.com)
>>>>>>> e9c445ad79c86b6a1112440305c06db448e0cd03
>>>>>>> 7a05e1896eebafd6f49b0e35d7c1fe950ec2e8f5

## Функционал:
- Узнать о SNMP
- Выбрать платформу
  - Frameworks
  - UI (GUI or CLI)
- Запусить протокол (чтобы работал)
- _Создать класс "Заголовок SNMP"?_
  - Поля:
    - Version
    - Community
    - PDU type
    - Request ID
    - Error status
    - Error index
    - Variable bindings
- Создать агента, следящего за устройством
  - Поля:
    - IP-адрес
    - Порт
  - Методы:
    - Start observing(observable object?)
    - Stop observing(observable object?)
    - On get requested(request info)
    - On set requested(request info)
    - Response(response info)
    - Trap(trap info)
- Создать менеджера
  - Поля:
    - IP-адрес
    - Порт
    - Timer
  - Методы:
    - Get(variables names)
    - Set(setted variables names, new variables values)
    - On response getted(responce info)
    - On trap getted(getted trap msg/var)
    - Timer time over/out/up
