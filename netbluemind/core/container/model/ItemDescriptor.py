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

class ItemDescriptor :
	def __init__( self):
		self.uid = None
		self.version = None
		self.displayName = None
		self.externalId = None
		self.internalId = None
		self.createdBy = None
		self.updatedBy = None
		self.created = None
		self.updated = None
		pass

class __ItemDescriptorSerDer__:
	def __init__( self ):
		pass

	def parse(self, value):
		if(value == None):
			return None
		instance = ItemDescriptor()

		self.parseInternal(value, instance)
		return instance

	def parseInternal(self, value, instance):
		uidValue = value['uid']
		instance.uid = serder.STRING.parse(uidValue)
		versionValue = value['version']
		instance.version = serder.LONG.parse(versionValue)
		displayNameValue = value['displayName']
		instance.displayName = serder.STRING.parse(displayNameValue)
		externalIdValue = value['externalId']
		instance.externalId = serder.STRING.parse(externalIdValue)
		internalIdValue = value['internalId']
		instance.internalId = serder.LONG.parse(internalIdValue)
		createdByValue = value['createdBy']
		instance.createdBy = serder.STRING.parse(createdByValue)
		updatedByValue = value['updatedBy']
		instance.updatedBy = serder.STRING.parse(updatedByValue)
		createdValue = value['created']
		instance.created = serder.DATE.parse(createdValue)
		updatedValue = value['updated']
		instance.updated = serder.DATE.parse(updatedValue)
		return instance

	def encode(self, value):
		if(value == None):
			return None
		instance = dict()
		self.encodeInternal(value,instance)
		return instance

	def encodeInternal(self, value, instance):

		uidValue = value.uid
		instance["uid"] = serder.STRING.encode(uidValue)
		versionValue = value.version
		instance["version"] = serder.LONG.encode(versionValue)
		displayNameValue = value.displayName
		instance["displayName"] = serder.STRING.encode(displayNameValue)
		externalIdValue = value.externalId
		instance["externalId"] = serder.STRING.encode(externalIdValue)
		internalIdValue = value.internalId
		instance["internalId"] = serder.LONG.encode(internalIdValue)
		createdByValue = value.createdBy
		instance["createdBy"] = serder.STRING.encode(createdByValue)
		updatedByValue = value.updatedBy
		instance["updatedBy"] = serder.STRING.encode(updatedByValue)
		createdValue = value.created
		instance["created"] = serder.DATE.encode(createdValue)
		updatedValue = value.updated
		instance["updated"] = serder.DATE.encode(updatedValue)
		return instance

