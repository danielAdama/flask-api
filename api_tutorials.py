import flask
import requests

# url = "https://jsonplaceholder.typicode.com/todos/1"
# response = requests.get(url)
# print(response.json())
# print(response.status_code)
# print(response.headers["Content-Type"])

url='https://jsonplaceholder.typicode.com/todos/'
todo = {"userId": 1, "title": "Buy milk", "completed": False}
response = requests.post(url=url, json=todo)
print(response.json())
print(response.status_code)

