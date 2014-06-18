#!/usr/bin/python
import requests
import xml.etree.ElementTree as ET

auth = {"apikey" : "api_str"}
base_url = "http://api.espn.com/v1/sports"

resp = requests.get(base_url, params=auth)
rc = int(resp.status_code)

sc = [200, 400, 401, 403, 404, 500, 504]
sc_r = ['Successful', 'Bad Request', 'Unuthorized', 'Account Over Quota', 'Not Found', 'Internal Server Error', 'TimeOut']

if rc == sc[0]:
	print sc_r[0]
elif rc == sc[1]:
	print "Request failed. Reason:" sc_r[1]
elif rc == sc[2]:
	print "Request failed. Reason:" sc_r[2]
elif rc == sc[3]:
	print "Request failed. Reason:" sc_r[3]
elif rc == sc[4]:
	print "Request failed. Reason:" sc_r[4]
elif rc == sc[5]:
	print "Request failed. Reason:" sc_r[5]
elif rc == sc[6]:
	print "Request failed. Reason:" sc_r[6]
elif rc not in sc:
	print "Request failed. Reason:" rc
