import scapy.all as scrapy

def sniff(interface):
    scrapy.sniff(iface=interface, store=False, prn=process_sniffed_packet, filter="sip")

def process_sniffed_packet(packet):
    print(packet)


sniff('Ethernet')#здесь должно быть название сетевого интерфейса, но я не могу его найти
