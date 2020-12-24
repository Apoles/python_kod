import requests
import json


result=requests.get("http://jsonplaceholder.typicode.com/todos")


result=json.loads(result.text)  
print(result[0]["title"])

for i in result:
    if i["userId"] == 1:
        print(i["title"])

print(type(result))

