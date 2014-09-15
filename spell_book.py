#!/usr/bin/env python
# -*- coding: utf-8 -*-

import yaml
import spell_book

conf_file = "./settings/myhome_conf.yaml"
f = open(conf_file, "r")
conf = yaml.load(f)	
f.close()

def get_orders_from_spell(spell):	
	if conf["spells"].has_key(spell):
		return conf["spells"][spell]
	else:
		return []

def get_data_from_order(order):
	if conf["orders"].has_key(order):
		return conf["orders"][order]
	else:
		print "This order is not registered"
		return None

