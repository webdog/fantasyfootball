#!/usr/bin/python
import urllib2, os, re

apipw = "apikeygoeshere"

print "This is the data gathering program for Weber's FF database."
print "Input 1 to begin, 0 to exit"
input = int(raw_input(">"))

if input == 1:
	info = urllib2.urlopen("http://api.espn.com/v1/sports/basketball/nba/teams/4?rostertype=active&_accept=text%%2Fxml&apikey=%s" % apipw)
	print info
else:
	print "Nothing!"
	
