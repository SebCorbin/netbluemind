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

class Restorable :
	def __init__( self):
		self.kind = None
		self.entryUid = None
		self.domainUid = None
		self.displayName = None
		pass

class __RestorableSerDer__:
	def __init__( self ):
		pass

	def parse(self, value):
		if(value == None):
			return None
		instance = Restorable()

		self.parseInternal(value, instance)
		return instance

	def parseInternal(self, value, instance):
		from netbluemind.dataprotect.api.RestorableKind import RestorableKind
		from netbluemind.dataprotect.api.RestorableKind import __RestorableKindSerDer__
		kindValue = value['kind']
		instance.kind = __RestorableKindSerDer__().parse(kindValue)
		entryUidValue = value['entryUid']
		instance.entryUid = serder.STRING.parse(entryUidValue)
		domainUidValue = value['domainUid']
		instance.domainUid = serder.STRING.parse(domainUidValue)
		displayNameValue = value['displayName']
		instance.displayName = serder.STRING.parse(displayNameValue)
		return instance

	def encode(self, value):
		if(value == None):
			return None
		instance = dict()
		self.encodeInternal(value,instance)
		return instance

	def encodeInternal(self, value, instance):

		from netbluemind.dataprotect.api.RestorableKind import RestorableKind
		from netbluemind.dataprotect.api.RestorableKind import __RestorableKindSerDer__
		kindValue = value.kind
		instance["kind"] = __RestorableKindSerDer__().encode(kindValue)
		entryUidValue = value.entryUid
		instance["entryUid"] = serder.STRING.encode(entryUidValue)
		domainUidValue = value.domainUid
		instance["domainUid"] = serder.STRING.encode(domainUidValue)
		displayNameValue = value.displayName
		instance["displayName"] = serder.STRING.encode(displayNameValue)
		return instance

