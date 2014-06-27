#!/usr/bin/python
import requests
import json
from pprint import pprint

def new_query():
	print "This is the data collection app that takes data from the ESPN api, and returns data to json format.\n"
	print "Please select the sports data you want:\n"
	x = int(raw_input("1. NHL\n2. NBA\n3. MLB\n4. NFL\n>"))
	valid_input = [int(1), int(2), int(3), int(4)]
	if x not in valid_input:
		print "Invalid selection. Exiting"
		exit()
	else:
		print "Passing request to API. Standby"
		gather_info(x)

def gather_info(x):
	auth = {"apikey" : ""}
	base_url = "http://api.espn.com/v1/sports"
	sp = {
			'fb': '/football/nfl/teams',
			'hk': '/hockey/nhl/teams',
			'bb': '/basketball/nba/teams',
			'bbl': '/baseball/mlb/teams'
			}
	uri = base_url

	if x == 1:
		uri = uri+sp['hk']
		print "Returning hockey results"
	elif x == 2:
		uri  = uri+sp['bb']
		print "Returning basketball results"
	elif x == 3:
		uri = uri+sp['bbl']
		print "Returning baseball results"
	elif x == 4:
		uri = uri+sp['fb']
		print "Returning football results"
	else:
		print "Unhandled exception, reason: %s" % x
		exit()

	resp = requests.get(uri, params=auth)
	rc = int(resp.status_code)

	#HTTP status codes
	sc = [int(200), int(400), int(401), int(403), int(404), int(500), int(504)]
	#Values of HTTP status codes, matched by position of sc
	sc_r = [str('Successful'), str('Bad Request'), str('Unauthorized'), str('Account Over Quota'), str('Not Found'), str('Internal Server Error'), str('TimeOut')]
	
	#Check if return code (rc) is 200 (First position of sc). If so, continue.
	if rc == sc[0]:
		print sc_r[0]
	#Assigns df object to resp.text wrapped in json loader
		df = json.loads(resp.text)
	#Accesses teams portion of json text
		team_names = df['sports'][0]['leagues'][0]['teams']
		for i in team_names:
	#Concatenates string value of location and name to output
			print i['location']+' '+i['name']
			
	
	#If API request fails the listed elifs will go through the list ofcommon HTTP responses and print out the response.  
	elif rc == sc[1]:
		print "Request failed. Reason: %s" % sc_r[1]
		exit()
	elif rc == sc[2]:
		print "Request failed. Reason: %s" % sc_r[2]
		exit()
	elif rc == sc[3]:
		print "Request failed. Reason: %s" % sc_r[3]
		exit()
	elif rc == sc[4]:
		print "Request failed. Reason: %s" % sc_r[4]
		exit()
	elif rc == sc[5]:
		print "Request failed. Reason: %s" % sc_r[5]
		exit()
	elif rc == sc[6]:
		print "Request failed. Reason: %s" % sc_r[6]
		exit()
	elif rc not in sc:
		print "Big failure. Reason: %i" % rc
		exit()
	else:
		"Unexpected Response. Exiting"
		exit()
	
if __name__ == "__main__":
	new_query()	
