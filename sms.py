#!/usr/bin/env python
 
import urllib.request
import urllib.parse
  
def sendSMS(apikey, numbers, message):
    params = {'apikey': apikey, 'numbers': numbers, 'message' : message }
    f = urllib.request.urlopen('https://api.textlocal.in/send/?'
        + urllib.parse.urlencode(params))
    return (f.read(), f.code)
  
resp, code = sendSMS('N8-K6J8xxZb3', '2828282819', 'Hi, welcome to the custom api service. This is a python application. Kindly feedback about this instant notification')
print (resp)
