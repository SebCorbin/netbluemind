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

class ContainerDescriptor :
	def __init__( self):
		self.uid = None
		self.name = None
		self.owner = None
		self.type = None
		self.defaultContainer = None
		self.writable = None
		self.verbs = None
		self.domainUid = None
		self.settings = None
		self.ownerDisplayname = None
		self.ownerDirEntryPath = None
		self.readOnly = None
		self.offlineSync = None
		pass

class __ContainerDescriptorSerDer__:
	def __init__( self ):
		pass

	def parse(self, value):
		if(value == None):
			return None
		instance = ContainerDescriptor()

		self.parseInternal(value, instance)
		return instance

	def parseInternal(self, value, instance):
		uidValue = value['uid']
		instance.uid = serder.STRING.parse(uidValue)
		nameValue = value['name']
		instance.name = serder.STRING.parse(nameValue)
		ownerValue = value['owner']
		instance.owner = serder.STRING.parse(ownerValue)
		typeValue = value['type']
		instance.type = serder.STRING.parse(typeValue)
		defaultContainerValue = value['defaultContainer']
		instance.defaultContainer = serder.BOOLEAN.parse(defaultContainerValue)
		writableValue = value['writable']
		instance.writable = serder.BOOLEAN.parse(writableValue)
		from netbluemind.core.container.model.acl.Verb import Verb
		from netbluemind.core.container.model.acl.Verb import __VerbSerDer__
		verbsValue = value['verbs']
		instance.verbs = serder.SetSerDer(__VerbSerDer__()).parse(verbsValue)
		domainUidValue = value['domainUid']
		instance.domainUid = serder.STRING.parse(domainUidValue)
		settingsValue = value['settings']
		instance.settings = serder.MapSerDer(serder.STRING).parse(settingsValue)
		ownerDisplaynameValue = value['ownerDisplayname']
		instance.ownerDisplayname = serder.STRING.parse(ownerDisplaynameValue)
		ownerDirEntryPathValue = value['ownerDirEntryPath']
		instance.ownerDirEntryPath = serder.STRING.parse(ownerDirEntryPathValue)
		readOnlyValue = value['readOnly']
		instance.readOnly = serder.BOOLEAN.parse(readOnlyValue)
		offlineSyncValue = value['offlineSync']
		instance.offlineSync = serder.BOOLEAN.parse(offlineSyncValue)
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
		nameValue = value.name
		instance["name"] = serder.STRING.encode(nameValue)
		ownerValue = value.owner
		instance["owner"] = serder.STRING.encode(ownerValue)
		typeValue = value.type
		instance["type"] = serder.STRING.encode(typeValue)
		defaultContainerValue = value.defaultContainer
		instance["defaultContainer"] = serder.BOOLEAN.encode(defaultContainerValue)
		writableValue = value.writable
		instance["writable"] = serder.BOOLEAN.encode(writableValue)
		from netbluemind.core.container.model.acl.Verb import Verb
		from netbluemind.core.container.model.acl.Verb import __VerbSerDer__
		verbsValue = value.verbs
		instance["verbs"] = serder.SetSerDer(__VerbSerDer__()).encode(verbsValue)
		domainUidValue = value.domainUid
		instance["domainUid"] = serder.STRING.encode(domainUidValue)
		settingsValue = value.settings
		instance["settings"] = serder.MapSerDer(serder.STRING).encode(settingsValue)
		ownerDisplaynameValue = value.ownerDisplayname
		instance["ownerDisplayname"] = serder.STRING.encode(ownerDisplaynameValue)
		ownerDirEntryPathValue = value.ownerDirEntryPath
		instance["ownerDirEntryPath"] = serder.STRING.encode(ownerDirEntryPathValue)
		readOnlyValue = value.readOnly
		instance["readOnly"] = serder.BOOLEAN.encode(readOnlyValue)
		offlineSyncValue = value.offlineSync
		instance["offlineSync"] = serder.BOOLEAN.encode(offlineSyncValue)
		return instance

