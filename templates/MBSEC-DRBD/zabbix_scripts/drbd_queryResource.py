#!/usr/bin/python
#coding: utf-8
import json
import sys
import subprocess

if len(sys.argv) == 2:
   item = sys.argv[1]
   arg = "status"
elif len(sys.argv) == 3:
   item = sys.argv[1]
   arg = sys.argv[2]
else:
   print "Syntax: ",sys.argv[0]," <resource-name> [cstate|dstate|syncstatus]"
   sys.exit(1)

def execCommand(command):
   comm = subprocess.check_output([command],shell=True)
   print comm.strip()
   sys.exit(0)

# The commands always should return a uniq value. 
if arg == 'cstate':
   cmd = 'drbdadm cstate %s' % item
elif arg == 'dstate':
   cmd = 'drbdadm dstate %s' % item
elif arg == 'syncstatus':
  #cmd = 'drbdadm status %s | awk -F\':\' \'/.*done:/ {print $4}\'' % item
  cmd = 'VALOR=$(drbdadm status %s | awk -F\':\' \'/.*done:/ {print $4}\'); if [ -z $VALOR ]; then echo \"100\"; else echo $VALOR; fi' % item
else:
   sys.exit(1)

execCommand(cmd)
