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

class Reminder :
	def __init__( self):
		self.vevent = None
		self.valarm = None
		pass

class __ReminderSerDer__:
	def __init__( self ):
		pass

	def parse(self, value):
		if(value == None):
			return None
		instance = Reminder()

		self.parseInternal(value, instance)
		return instance

	def parseInternal(self, value, instance):
		from netbluemind.calendar.api.VEvent import VEvent
		from netbluemind.calendar.api.VEvent import __VEventSerDer__
		from netbluemind.core.container.model.ItemValue import ItemValue
		from netbluemind.core.container.model.ItemValue import __ItemValueSerDer__
		veventValue = value['vevent']
		instance.vevent = __ItemValueSerDer__(__VEventSerDer__()).parse(veventValue)
		from netbluemind.icalendar.api.ICalendarElementVAlarm import ICalendarElementVAlarm
		from netbluemind.icalendar.api.ICalendarElementVAlarm import __ICalendarElementVAlarmSerDer__
		valarmValue = value['valarm']
		instance.valarm = __ICalendarElementVAlarmSerDer__().parse(valarmValue)
		return instance

	def encode(self, value):
		if(value == None):
			return None
		instance = dict()
		self.encodeInternal(value,instance)
		return instance

	def encodeInternal(self, value, instance):

		from netbluemind.calendar.api.VEvent import VEvent
		from netbluemind.calendar.api.VEvent import __VEventSerDer__
		from netbluemind.core.container.model.ItemValue import ItemValue
		from netbluemind.core.container.model.ItemValue import __ItemValueSerDer__
		veventValue = value.vevent
		instance["vevent"] = __ItemValueSerDer__(__VEventSerDer__()).encode(veventValue)
		from netbluemind.icalendar.api.ICalendarElementVAlarm import ICalendarElementVAlarm
		from netbluemind.icalendar.api.ICalendarElementVAlarm import __ICalendarElementVAlarmSerDer__
		valarmValue = value.valarm
		instance["valarm"] = __ICalendarElementVAlarmSerDer__().encode(valarmValue)
		return instance

