#!/usr/bin/env python
# -*- coding: utf-8 -*-

class SpellBook:
	def __init__(self, spells, orders):		
		self.spell_list = spells
		self.order_list = orders

	def get_orders_from_spell(self, spell):	
		if self.spell_list.has_key(spell):
			return self.spell_list[spell]
		else:
			return []
	
	def get_data_from_order(self, order):
		if self.order_list.has_key(order):
			return self.order_list[order]
		else:
			print "This order is not registered"
			return None
	
