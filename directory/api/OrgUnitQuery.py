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

class OrgUnitQuery :
	def __init__( self):
		self.from_ = None
		self.size = None
		self.query = None
		self.managableKinds = None
		pass

class __OrgUnitQuerySerDer__:
	def __init__( self ):
		pass

	def parse(self, value):
		if(value == None):
			return None
		instance = OrgUnitQuery()

		self.parseInternal(value, instance)
		return instance

	def parseInternal(self, value, instance):
		from_Value = value['from']
		instance.from_ = serder.INT.parse(from_Value)
		sizeValue = value['size']
		instance.size = serder.INT.parse(sizeValue)
		queryValue = value['query']
		instance.query = serder.STRING.parse(queryValue)
		from netbluemind.directory.api.DirEntryKind import DirEntryKind
		from netbluemind.directory.api.DirEntryKind import __DirEntryKindSerDer__
		managableKindsValue = value['managableKinds']
		instance.managableKinds = serder.SetSerDer(__DirEntryKindSerDer__()).parse(managableKindsValue)
		return instance

	def encode(self, value):
		if(value == None):
			return None
		instance = dict()
		self.encodeInternal(value,instance)
		return instance

	def encodeInternal(self, value, instance):

		from_Value = value.from_
		instance["from"] = serder.INT.encode(from_Value)
		sizeValue = value.size
		instance["size"] = serder.INT.encode(sizeValue)
		queryValue = value.query
		instance["query"] = serder.STRING.encode(queryValue)
		from netbluemind.directory.api.DirEntryKind import DirEntryKind
		from netbluemind.directory.api.DirEntryKind import __DirEntryKindSerDer__
		managableKindsValue = value.managableKinds
		instance["managableKinds"] = serder.SetSerDer(__DirEntryKindSerDer__()).encode(managableKindsValue)
		return instance

