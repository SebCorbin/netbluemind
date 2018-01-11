#
#  BEGIN LICENSE
#  Copyright (c) Blue Mind SAS, 2012-2016
# 
#  This file is part of BlueMind. BlueMind is a messaging and collaborative
#  solution.
# 
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of either the GNU Affero General Public License as
#  published by the Free Software Foundation (version 3 of the License).
# 
# 
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
# 
#  See LICENSE.txt
#  END LICENSE
#
import requests
from netbluemind.python import serder

class Server :
	def __init__( self):
		self.ip = None
		self.fqdn = None
		self.name = None
		self.tags = None
		pass

class __ServerSerDer__:
	def __init__( self ):
		pass

	def parse(self, value):
		if(value == None):
			return None
		instance = Server()

		self.parseInternal(value, instance)
		return instance

	def parseInternal(self, value, instance):
		ipValue = value['ip']
		instance.ip = serder.STRING.parse(ipValue)
		fqdnValue = value['fqdn']
		instance.fqdn = serder.STRING.parse(fqdnValue)
		nameValue = value['name']
		instance.name = serder.STRING.parse(nameValue)
		tagsValue = value['tags']
		instance.tags = serder.ListSerDer(serder.STRING).parse(tagsValue)
		return instance

	def encode(self, value):
		if(value == None):
			return None
		instance = dict()
		self.encodeInternal(value,instance)
		return instance

	def encodeInternal(self, value, instance):

		ipValue = value.ip
		instance["ip"] = serder.STRING.encode(ipValue)
		fqdnValue = value.fqdn
		instance["fqdn"] = serder.STRING.encode(fqdnValue)
		nameValue = value.name
		instance["name"] = serder.STRING.encode(nameValue)
		tagsValue = value.tags
		instance["tags"] = serder.ListSerDer(serder.STRING).encode(tagsValue)
		return instance

