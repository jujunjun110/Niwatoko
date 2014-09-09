#!/usr/bin/env python
# -*- coding: utf-8 -*-

class IRKitManager:
	def __init__(self):
		self.ip = "192.168.11.23"
	
	def sendData(self, data):
		import httplib, urllib

		params = 'message=' + data
		headers = {"Content-type": "application/x-www-form-urlencoded", "Accept": "text/plain"}
		conn = httplib.HTTPConnection(self.ip)
		conn.request("POST", "/messages", params, headers)
		response = conn.getresponse()
		print response.status, response.reason
		
