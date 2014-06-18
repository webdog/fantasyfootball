#!/usr/bin/python
import requests
import xml.etree.ElementTree as ET

apikey = ""
v = "v1"
base_url = "http://api.espn.com/"

all_sports_req = base_url+v+"/sports?apikey="+apikey

resp = requests.get(all_sports_req)

if "200" in str(resp):
	print "API request succeeded"
else:
	print "API success failed. Reason:"
	print resp

