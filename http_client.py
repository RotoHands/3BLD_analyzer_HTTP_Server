import http.client
import json

conn = http.client.HTTPSConnection('127.0.0.1:8080')

headers = {'Content-type': 'application/json'}

foo = {'text': 'Hello HTTP #1 **cool**, and #1!'}
json_data = json.dumps(foo)

conn.request('POST', '/post', json_data, headers)

response = conn.getresponse()
print(response.read().decode())