import requests

URL = 'http://203.237.53.5:8000/tower/api/'
person_id = '1f4b466a-c903-45b0-8724-7cb46e95d709'
nuc_id = 1
image = open('person.jpg', 'rb')

data = {
        'match_rate': 98,
        'person': '1f4b466a-c903-45b0-8724-7cb46e95d709',
        'detected_nuc': '1'
        }

files = {
        'image': image
        }

response = requests.post(URL, data = data, files=files)
print(response.content)
