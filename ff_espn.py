#!/usr/bin/python
import requests
import xml.etree.ElementTree as ET

def new_query():
	print "This is the data collection app that takes data from the ESPN api, and returns data to json format.\n"
	print "Please select the sports data you want:\n"
	x = raw_input("1. NHL\n2. NBA\n3. MLB\n4."i)
	input_list = int([1, 2, 3, 4])
	if x not in input_list:
		print "Invalid selection. Exiting"
		exit()
	else:
		print "Passing request to API. Standby"

def gather_info(x):

	auth = {"apikey" : "api_str"}
	base_url = "http://api.espn.com/v1/sports"

	resp = requests.get(base_url, params=auth)
	rc = int(resp.status_code)

	#HTTP status codes
	sc = int([
			200, 
			400, 
			401, 
			403, 
			404, 
			500, 
			504
			])
	#Values of HTTP status codes, matched by position of sc
	sc_r = [
			'Successful', 
			'Bad Request', 
			'Unuthorized', 
			'Account Over Quota', 
			'Not Found', 
			'Internal Server Error', 
			'TimeOut'i
			]
	
	#Check if return code (rc) is 200 (First position of sc). If so, continue.
	if rc == sc[0]:
		print sc_r[0]
	
	#If API request fails the listed elifs will go through the list of common HTTP responses and print out the response.
	elif rc == sc[1]:
		print "Request failed. Reason:" sc_r[1]
		exit()
	elif rc == sc[2]:
		print "Request failed. Reason:" sc_r[2]
		exit()
	elif rc == sc[3]:
		print "Request failed. Reason:" sc_r[3]
		exit()
	elif rc == sc[4]:
		print "Request failed. Reason:" sc_r[4]
		exit()
	elif rc == sc[5]:
		print "Request failed. Reason:" sc_r[5]
		exit()
	elif rc == sc[6]:
		print "Request failed. Reason:" sc_r[6]
		exit()
	elif rc not in sc:
		print "Request failed. Reason:" rc
		exit()
	else:
		"Unexpected Response. Exiting"
		exit()


if name == "__main__":
	new_query()
	gather_info(new_query(x))

