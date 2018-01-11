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

class CalendarDescriptor :
	def __init__( self):
		self.name = None
		self.domainUid = None
		self.settings = None
		self.owner = None
		self.orgUnitUid = None
		pass

class __CalendarDescriptorSerDer__:
	def __init__( self ):
		pass

	def parse(self, value):
		if(value == None):
			return None
		instance = CalendarDescriptor()

		self.parseInternal(value, instance)
		return instance

	def parseInternal(self, value, instance):
		nameValue = value['name']
		instance.name = serder.STRING.parse(nameValue)
		domainUidValue = value['domainUid']
		instance.domainUid = serder.STRING.parse(domainUidValue)
		settingsValue = value['settings']
		instance.settings = serder.MapSerDer(serder.STRING).parse(settingsValue)
		ownerValue = value['owner']
		instance.owner = serder.STRING.parse(ownerValue)
		orgUnitUidValue = value['orgUnitUid']
		instance.orgUnitUid = serder.STRING.parse(orgUnitUidValue)
		return instance

	def encode(self, value):
		if(value == None):
			return None
		instance = dict()
		self.encodeInternal(value,instance)
		return instance

	def encodeInternal(self, value, instance):

		nameValue = value.name
		instance["name"] = serder.STRING.encode(nameValue)
		domainUidValue = value.domainUid
		instance["domainUid"] = serder.STRING.encode(domainUidValue)
		settingsValue = value.settings
		instance["settings"] = serder.MapSerDer(serder.STRING).encode(settingsValue)
		ownerValue = value.owner
		instance["owner"] = serder.STRING.encode(ownerValue)
		orgUnitUidValue = value.orgUnitUid
		instance["orgUnitUid"] = serder.STRING.encode(orgUnitUidValue)
		return instance

