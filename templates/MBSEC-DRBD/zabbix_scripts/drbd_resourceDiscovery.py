#!/usr/bin/python
#coding: utf-8
import json
import sys
import subprocess

if len(sys.argv) != 2:
   print "Syntax: ",sys.argv[0]," resource"
   sys.exit(1)
else:
   item = sys.argv[1]

# System command to get the info.
def execCommand(command):
   comm = subprocess.check_output([command],shell=True)
   return comm

if item == 'resource':
   cmd='drbdadm dump-xml | awk -F\'"\' \'/<resource name=/ { print $2}\''
else:
   print "No right item"
   sys.exit(1)

result=execCommand(cmd)

# Starts the array.
data = {}
data['data'] = []

for row in result.split('\n'):			# For each "line",
   if row is not "":				# The last row is blank.
      data['data'].append({
         '{#RESOURCE}': row,
      })

# Print the results in JSON format.
json.dump(data, sys.stdout)
