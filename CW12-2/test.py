import requests

# response=requests.post('http://192.168.1.105:9999/',
#             json={'id':2, 'title': 'school','description':'study'})
# print(response.text)

response = requests.get('http://192.168.1.105:9999/')
print(response.json())