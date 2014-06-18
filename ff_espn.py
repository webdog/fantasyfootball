#!/usr/bin/python
import requests
import xml.etree.ElementTree as ET

auth = {"apikey": "api_key_str"}
base_url = "http://api.espn.com/v1/sports"

resp = requests.get(base_url, params=auth)
sc = int(resp.status_code)

if sc == 200:
	print resp.text
else:
	print "API success failed. Reason:"
	print resp

