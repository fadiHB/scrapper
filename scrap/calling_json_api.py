# Using the GeoJSON API
# Week 6

# import json
# import urllib.request

# #Stroring the given parameters
# serviceurl = "http://py4e-data.dr-chuck.net/json?"
# sample_address = "South Federal University"
# data_address = "Columbia University"
# address_wanted = data_address

# #Setting the GET parameters on the URL
# parameters = {"address": address_wanted}
# paramsurl = urllib.request.urlopen(parameters)

# #Generating the complete URL. Printing it in order to check if it's correct.
# queryurl = serviceurl + paramsurl
# print("DATA URL: ", queryurl)

# #Obtaining and reading the data
# data = urllib.request.urlopen(queryurl).read()

# #Parsing the data and looking for the field we want.
# #That field is inside the "Results" array, in its first item (if our address is 
# #correct we can assume that the result would be the correct one) and on its 
# #"place_id" field
# jsondata = json.loads(str(data))
# place_id = jsondata["results"][0]["place_id"]
# print("PLACE ID: ", place_id)


import urllib.request
import urllib.parse
import json


api = "http://py4e-data.dr-chuck.net/json?"

address = input( "Enter Address: " ) or 'Malayer Azad University'

params = { "key": 42, "address": address }
url = api + urllib.parse.urlencode(params)
print(url)

response = urllib.request.urlopen(url)
data = response.read().decode('utf-8')

json_data = json.loads(data)

place_id = json_data["results"][0]["place_id"]
print("Place id", place_id)