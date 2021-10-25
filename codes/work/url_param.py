#python

import requests

url = "http://www.yahoo.com"

params = {}

response = requests.get(url)

print(response)
