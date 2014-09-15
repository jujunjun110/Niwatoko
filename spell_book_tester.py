#!/usr/bin/env python
# -*- coding: utf-8 -*-
# spellbookが正常に動くか確かめるための簡易的なテスト

def main():	
	from irkit_manager import IRKitManager
	import yaml
	import spell_book

	conf_file = "./myhome_conf.yaml"
	f = open(conf_file, "r")
	conf = yaml.load(f)	
	f.close()
	
	ip = conf["ip"]
	irk = IRKitManager(ip)
	
	spell = u"おはよう"
	
	orders = spell_book.get_orders_from_spell(spell)

	print orders[1]
	
	for order in orders:
		data = spell_book.get_data_from_order(order)
		print "data: " + data
		irk.send_data(data)
	
if __name__ == "__main__":
	main()
