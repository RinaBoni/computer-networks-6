#!/usr/bin/env python

import scapy.all as sc
import argparse as ap


def get_arguments():
	parser = ap.ArgumentParser()
	parser.add_argument("-t", "--target", dest="target", help="Target IP/IP range.")
	options = parser.parse_args()
	return options


def scan(ip):
	arp_request = sc.ARP(pdst=ip)
	broadcast = sc.Ether(dst="ff:ff:ff:ff:ff:ff")
	arp_request_broadcast = broadcast/arp_request
	answerd_list = sc.srp(arp_request_broadcast, timeout=1, verbose=False)[0]
	
	client_list = []
	for element in answerd_list:
		client_dict = {"ip": element[1].psrc, "mac":element[1].hwsrc}
		client_list.append(client_dict)
	return client_list


def print_result(result_list):
	print("IP\t\t\tMAC address\n---------------------------------------------------------")
	for client in result_list:
		print(client["ip"] + "\t\t" + client["mac"])



options = get_arguments()
scan_result = scan(options.target)
print_result(scan_result)

