import requests

URL = 'http://203.237.53.5:8000/tower/api/'
response = requests.get(URL)
print(response.content)

