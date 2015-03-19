#!/usr/bin/python
#./ping.py www.example.com

import os
import sys
hostname = sys.argv[1]

print 'I\'m pinging, Please wait...'

checkhostalive = os.system('ping -c 5 ' + hostname + '> /dev/null 2>&1')

if checkhostalive == 0:
	print hostname + ' is up.'
else:
	print hostname + ' is down.!!!'
