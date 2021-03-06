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

class RolesCategory :
	def __init__( self):
		self.id = None
		self.label = None
		pass

class __RolesCategorySerDer__:
	def __init__( self ):
		pass

	def parse(self, value):
		if(value == None):
			return None
		instance = RolesCategory()

		self.parseInternal(value, instance)
		return instance

	def parseInternal(self, value, instance):
		idValue = value['id']
		instance.id = serder.STRING.parse(idValue)
		labelValue = value['label']
		instance.label = serder.STRING.parse(labelValue)
		return instance

	def encode(self, value):
		if(value == None):
			return None
		instance = dict()
		self.encodeInternal(value,instance)
		return instance

	def encodeInternal(self, value, instance):

		idValue = value.id
		instance["id"] = serder.STRING.encode(idValue)
		labelValue = value.label
		instance["label"] = serder.STRING.encode(labelValue)
		return instance

