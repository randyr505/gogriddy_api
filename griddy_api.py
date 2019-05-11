#!/usr/bin/python

import os
import ConfigParser
import json
import urllib2
import requests

dir_name = os.path.dirname(os.path.realpath(__file__))
conf = dir_name + '/config.cf'

config = ConfigParser.ConfigParser()
config.read(conf)

meterID = config.get('default', 'meterID')
memberID = config.get('default', 'memberID')
settlement_point = config.get('default', 'settlement_point')
api_url = config.get('default', 'api_url')

data = {'meterID': meterID, 'memberID': memberID, 'settlement_point': settlement_point}
r = requests.post(api_url, data=json.dumps(data))

#print "response code=", r
#print r.text
j = json.loads(r.text)

print j["now"]["price_ckwh"],j["now"]["price_display_sign"], "per kwh"
