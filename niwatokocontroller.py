#!/usr/bin/env python
# -*- coding: utf-8 -*-

def main():
	import socket, sys, select

	from irkitmanager import IRKitManager
	import myhomeconf
	import spellbook

	ip = myhomeconf.ip
	IRkit = IRKitManager(ip)
	
	host = "localhost"
	port = 10500
	addr = (host,port)
	client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	client_socket.connect(addr)
	
	recMode = False
	recBuf = ""
	while True:
			data = client_socket.recv(80)
			if not data:
				print 'Shutting down.'
				break
			else:
				if "<RECOGOUT>" in data:
					recBuf = data
					recMode = True

				elif "</RECOGOUT>" in data:
					recBuf = recBuf + data 
					spell = get_sentence(recBuf) 
					spell = spell.decode('utf-8')
					print spell
	
					orders = spellbook.getOrdersFromSpell(spell)
					for order in orders:
						data = spellbook.getDataFromOrder(order)
						IRkit.sendData(data)
	
				elif recMode:
					recBuf = recBuf + data
	
	client_socket.close()


def get_sentence(recBuf):
	
	word = ""

	index_start = recBuf.find("<RECOGOUT>")
	index_end   = recBuf.find("</RECOGOUT>") + 11

	lines  = recBuf[index_start:index_end].splitlines()

	# 最初・最後の3行ずつは必ず不要な行
	for i in range(3, len(lines) - 3):
		index_word  = lines[i].find("WORD=")
		index_class = lines[i].find("CLASSID=")
		index_cm    = lines[i].find("CM=")
		
		word  = word + lines[i][index_word + 6:index_class - 2]
		
	return word

if __name__ == "__main__":
	main()
