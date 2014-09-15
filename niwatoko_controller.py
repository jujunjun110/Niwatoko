#!/usr/bin/env python
# -*- coding: utf-8 -*-

def main():
	import socket, sys, select, yaml

	from irkit_manager import IRKitManager
	import spell_book

	conf_file = "./myhome_conf.yaml"
	f = open(conf_file, "r")
	conf = yaml.load(f)	
	f.close()
	
	ip = conf["ip"]
	IRkit = IRKitManager(ip)
	
	host = "localhost"
	port = 10500
	addr = (host,port)
	client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	client_socket.connect(addr)
	
	rec_mode = False
	rec_buf = ""
	while True:
			data = client_socket.recv(80)
			if not data:
				print 'Shutting down.'
				break
			else:
				if "<RECOGOUT>" in data:
					rec_buf = data
					rec_mode = True

				elif "</RECOGOUT>" in data:
					rec_buf = rec_buf + data 
					spell = get_sentence(rec_buf) 
					spell = spell.decode('utf-8')
					print spell
	
					orders = spell_book.get_orders_from_spell(spell)
					for order in orders:
						data = spell_book.get_data_from_order(order)
						if data is not None:
							IRkit.send_data(data)
	
				elif rec_mode:
					rec_buf = rec_buf + data
	
	client_socket.close()


def get_sentence(rec_buf):
	
	word = ""
	index_start = rec_buf.find("<RECOGOUT>")
	index_end   = rec_buf.find("</RECOGOUT>") + 11
	lines  = rec_buf[index_start:index_end].splitlines()

	for line in lines:
		index_word  = line.find("WORD=")
		index_class = line.find("CLASSID=")
		index_cm    = line.find("CM=")
		
		if index_word != -1 and index_class != -1:
			word  = word + line[index_word + 6:index_class - 2]

	return word

if __name__ == "__main__":
	main()
