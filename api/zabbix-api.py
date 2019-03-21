#!/usr/bin/python
# -*- coding: utf-8 -*-

# Author: Marcus Burghardt
# marcus.apb@gmail.com
# License: MIT
#
# Python script to interact with Zabbix API.
# I created this script to make my life easier exporting templates
# in JSON format, to be used with Ansible zabbix_template module.
# But, for sure, this script could be customized to do any interaction with Zabbix API.
#
# More informations about Zabbix API:
# https://www.zabbix.com/documentation/3.4/manual/api/reference

import json
from zabbix_api import ZabbixAPI

# Connection informations
zabbix_server = "http://zabbix.domain.com"
username = "Admin"
password = "password"

# Connect!
#zapi = ZabbixAPI(server=zabbix_server, log_level=6)
zapi = ZabbixAPI(server=zabbix_server)
zapi.login(username, password)

########## 
# HOSTS 
########## 
#hosts = zapi.host.get({"output": "extend", "sortfield": "name"})
#for x in hosts:
#  print x['available'], "-", x['hostid'], "-", x['name']


########## 
# TEMPLATES 
########## 
template_name = "Template MBSEC - App Bacula" 

# Get all templates with ids
#templates = zapi.template.get({"output": "extend", "sortfield": "name"})
#for x in templates:
#  print x['templateid'], "-", x['name']

# To export a template, first get the id.
template = zapi.template.get({"output": "extend", "sortfield": "name",  "filter": { "host": template_name }})
template_id = template[0]['templateid']

# With the ID, exports the template configuration.
template = zapi.configuration.export({"options": { "templates": [ template_id ] }, "format": "json" })

# The normal output is a quite ugly. Let's turn it more human friendly. : )
# This permits direct the output to a file easier.
parsed = json.loads(template)
print json.dumps(parsed, indent=2, sort_keys=True)
