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
import json
from netbluemind.python import serder
from netbluemind.python.client import BaseEndpoint

IFolderHierarchy_VERSION = "3.1.25071"

class IFolderHierarchy(BaseEndpoint):
	def __init__(self, apiKey, url ,mailboxUid ):
		self.url = url
		self.apiKey = apiKey
		self.base = url +'/folders/{mailboxUid}'
		self.mailboxUid_ = mailboxUid
		self.base = self.base.replace('{mailboxUid}',mailboxUid)

	def multipleGet (self, uids ):
		postUri = "/_mget";
		__data__ = None
		__data__ = serder.ListSerDer(serder.STRING).encode(uids)

		queryParams = {   };

		response = requests.post( self.base + postUri, params = queryParams, verify=False, headers = {'X-BM-ApiKey' : self.apiKey, 'Accept' : 'application/json', 'X-BM-ClientVersion' : IFolderHierarchy_VERSION}, data = json.dumps(__data__));
		from netbluemind.folder.api.Folder import Folder
		from netbluemind.folder.api.Folder import __FolderSerDer__
		from netbluemind.core.container.model.ItemValue import ItemValue
		from netbluemind.core.container.model.ItemValue import __ItemValueSerDer__
		return self.handleResult__(serder.ListSerDer(__ItemValueSerDer__(__FolderSerDer__())), response)
	def byUid (self, uid ):
		postUri = "/by_uid";
		__data__ = None
		queryParams = {  'uid': uid   };

		response = requests.get( self.base + postUri, params = queryParams, verify=False, headers = {'X-BM-ApiKey' : self.apiKey, 'Accept' : 'application/json', 'X-BM-ClientVersion' : IFolderHierarchy_VERSION}, data = json.dumps(__data__));
		from netbluemind.folder.api.Folder import Folder
		from netbluemind.folder.api.Folder import __FolderSerDer__
		from netbluemind.core.container.model.ItemValue import ItemValue
		from netbluemind.core.container.model.ItemValue import __ItemValueSerDer__
		return self.handleResult__(__ItemValueSerDer__(__FolderSerDer__()), response)
	def allUids (self):
		postUri = "/_alluids";
		__data__ = None
		queryParams = {  };

		response = requests.get( self.base + postUri, params = queryParams, verify=False, headers = {'X-BM-ApiKey' : self.apiKey, 'Accept' : 'application/json', 'X-BM-ClientVersion' : IFolderHierarchy_VERSION}, data = json.dumps(__data__));
		return self.handleResult__(serder.ListSerDer(serder.STRING), response)
	def byParentId (self, parent ):
		postUri = "/by_parent_id";
		__data__ = None
		queryParams = {  'parent': parent   };

		response = requests.get( self.base + postUri, params = queryParams, verify=False, headers = {'X-BM-ApiKey' : self.apiKey, 'Accept' : 'application/json', 'X-BM-ClientVersion' : IFolderHierarchy_VERSION}, data = json.dumps(__data__));
		from netbluemind.folder.api.Folder import Folder
		from netbluemind.folder.api.Folder import __FolderSerDer__
		from netbluemind.core.container.model.ItemValue import ItemValue
		from netbluemind.core.container.model.ItemValue import __ItemValueSerDer__
		return self.handleResult__(serder.ListSerDer(__ItemValueSerDer__(__FolderSerDer__())), response)
	def changelog (self, since ):
		postUri = "/_changelog";
		__data__ = None
		__data__ = serder.LONG.encode(since)

		queryParams = {   };

		response = requests.get( self.base + postUri, params = queryParams, verify=False, headers = {'X-BM-ApiKey' : self.apiKey, 'Accept' : 'application/json', 'X-BM-ClientVersion' : IFolderHierarchy_VERSION}, data = json.dumps(__data__));
		from netbluemind.core.container.model.ContainerChangelog import ContainerChangelog
		from netbluemind.core.container.model.ContainerChangelog import __ContainerChangelogSerDer__
		return self.handleResult__(__ContainerChangelogSerDer__(), response)
	def byName (self, folderName ):
		postUri = "/by_name";
		__data__ = None
		queryParams = {  'folderName': folderName   };

		response = requests.get( self.base + postUri, params = queryParams, verify=False, headers = {'X-BM-ApiKey' : self.apiKey, 'Accept' : 'application/json', 'X-BM-ClientVersion' : IFolderHierarchy_VERSION}, data = json.dumps(__data__));
		from netbluemind.folder.api.Folder import Folder
		from netbluemind.folder.api.Folder import __FolderSerDer__
		from netbluemind.core.container.model.ItemValue import ItemValue
		from netbluemind.core.container.model.ItemValue import __ItemValueSerDer__
		return self.handleResult__(__ItemValueSerDer__(__FolderSerDer__()), response)
	def changeset (self, since ):
		postUri = "/_changeset";
		__data__ = None
		queryParams = {  'since': since   };

		response = requests.get( self.base + postUri, params = queryParams, verify=False, headers = {'X-BM-ApiKey' : self.apiKey, 'Accept' : 'application/json', 'X-BM-ClientVersion' : IFolderHierarchy_VERSION}, data = json.dumps(__data__));
		from netbluemind.core.container.model.ContainerChangeset import ContainerChangeset
		from netbluemind.core.container.model.ContainerChangeset import __ContainerChangesetSerDer__
		return self.handleResult__(__ContainerChangesetSerDer__(serder.STRING), response)
	def changesetById (self, since ):
		postUri = "/_changesetById";
		__data__ = None
		queryParams = {  'since': since   };

		response = requests.get( self.base + postUri, params = queryParams, verify=False, headers = {'X-BM-ApiKey' : self.apiKey, 'Accept' : 'application/json', 'X-BM-ClientVersion' : IFolderHierarchy_VERSION}, data = json.dumps(__data__));
		from netbluemind.core.container.model.ContainerChangeset import ContainerChangeset
		from netbluemind.core.container.model.ContainerChangeset import __ContainerChangesetSerDer__
		return self.handleResult__(__ContainerChangesetSerDer__(serder.LONG), response)
	def getComplete (self, uid ):
		postUri = "/{uid}/complete";
		__data__ = None
		postUri = postUri.replace("{uid}",uid);
		queryParams = {   };

		response = requests.get( self.base + postUri, params = queryParams, verify=False, headers = {'X-BM-ApiKey' : self.apiKey, 'Accept' : 'application/json', 'X-BM-ClientVersion' : IFolderHierarchy_VERSION}, data = json.dumps(__data__));
		from netbluemind.folder.api.Folder import Folder
		from netbluemind.folder.api.Folder import __FolderSerDer__
		from netbluemind.core.container.model.ItemValue import ItemValue
		from netbluemind.core.container.model.ItemValue import __ItemValueSerDer__
		return self.handleResult__(__ItemValueSerDer__(__FolderSerDer__()), response)
	def search (self, query ):
		postUri = "/_search";
		__data__ = None
		from netbluemind.folder.api.FolderQuery import FolderQuery
		from netbluemind.folder.api.FolderQuery import __FolderQuerySerDer__
		__data__ = __FolderQuerySerDer__().encode(query)

		queryParams = {   };

		response = requests.post( self.base + postUri, params = queryParams, verify=False, headers = {'X-BM-ApiKey' : self.apiKey, 'Accept' : 'application/json', 'X-BM-ClientVersion' : IFolderHierarchy_VERSION}, data = json.dumps(__data__));
		from netbluemind.folder.api.Folder import Folder
		from netbluemind.folder.api.Folder import __FolderSerDer__
		from netbluemind.core.container.model.ItemValue import ItemValue
		from netbluemind.core.container.model.ItemValue import __ItemValueSerDer__
		from netbluemind.core.api.ListResult import ListResult
		from netbluemind.core.api.ListResult import __ListResultSerDer__
		return self.handleResult__(__ListResultSerDer__(__ItemValueSerDer__(__FolderSerDer__())), response)
	def reset (self):
		postUri = "/_reset";
		__data__ = None
		queryParams = {  };

		response = requests.post( self.base + postUri, params = queryParams, verify=False, headers = {'X-BM-ApiKey' : self.apiKey, 'Accept' : 'application/json', 'X-BM-ClientVersion' : IFolderHierarchy_VERSION}, data = json.dumps(__data__));
		return self.handleResult__(None, response)
	def byContentUri (self, uri ):
		postUri = "/by_uri";
		__data__ = None
		queryParams = {  'uri': uri   };

		response = requests.get( self.base + postUri, params = queryParams, verify=False, headers = {'X-BM-ApiKey' : self.apiKey, 'Accept' : 'application/json', 'X-BM-ClientVersion' : IFolderHierarchy_VERSION}, data = json.dumps(__data__));
		from netbluemind.folder.api.Folder import Folder
		from netbluemind.folder.api.Folder import __FolderSerDer__
		from netbluemind.core.container.model.ItemValue import ItemValue
		from netbluemind.core.container.model.ItemValue import __ItemValueSerDer__
		return self.handleResult__(__ItemValueSerDer__(__FolderSerDer__()), response)
	def byId (self, id ):
		postUri = "/by_id";
		__data__ = None
		queryParams = {  'id': id   };

		response = requests.get( self.base + postUri, params = queryParams, verify=False, headers = {'X-BM-ApiKey' : self.apiKey, 'Accept' : 'application/json', 'X-BM-ClientVersion' : IFolderHierarchy_VERSION}, data = json.dumps(__data__));
		from netbluemind.folder.api.Folder import Folder
		from netbluemind.folder.api.Folder import __FolderSerDer__
		from netbluemind.core.container.model.ItemValue import ItemValue
		from netbluemind.core.container.model.ItemValue import __ItemValueSerDer__
		return self.handleResult__(__ItemValueSerDer__(__FolderSerDer__()), response)
