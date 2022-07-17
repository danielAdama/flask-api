from email import header
import flask
import requests
import json

# url = "https://jsonplaceholder.typicode.com/todos/1"
# response = requests.get(url)
# print(response.json())
# print(response.status_code)
# print(response.headers["Content-Type"])

## Post a data 1st process
# url='https://jsonplaceholder.typicode.com/todos/'
# todo = {"userId": 1, "title": "Buy milk", "completed": False}
# header = {"Content-Type":"application/json"}
# response = requests.post(url=url, data=json.dumps(todo), headers=header)
# print(response.json())
# print(response.status_code)

## Post a data 2nd process
# url='https://jsonplaceholder.typicode.com/todos/'
# todo = {'userId': 1, 'title': 'Wash car', 'completed': True, 'id': 10}
# header = {"Content-Type":"application/json"}
# response = requests.post(url=url, data=json.dumps(todo), headers=header)
# print(response.json())
# print(response.status_code)

## Patch to modify an entry
# url='https://jsonplaceholder.typicode.com/todos/10'
# todo = {"title": "Mow lawn"}
# response = requests.patch(url=url, json=todo)
# print(response.json())
# print(response.status_code)

# Delete to remove an entry
url='https://jsonplaceholder.typicode.com/todos/10'
response = requests.delete(url=url)
print(response.json())
print(response.status_code)