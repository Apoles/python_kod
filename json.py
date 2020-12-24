"""import re
dosya=open("ali.txt","r",encoding="utf-8")
b=dosya.read()
print(b)
a=re.findall("\S",b)
print(a)"""



"""
#json yapısı
import json

person_string='{"name":"ali","languages":["python","c#"]}'
print(type(person_string))
#Result=person["name"]

result=json.loads(person_string) #json string to dict

result=result["languages"]
print(result)
print(type(result)) """

#dosyadan json okuma
"""import json 

person_string='{"name":"ali","languages":["python","c#"]}'

with open("ah.py") as f:
    data=json.load(f)
    print(data["name"])
    print(data["languages"])"""

import json
person_string='{"name":"ali","languages":["python","c#"]}'
person_dict={
    "name":"ali",
    "languages":["c#","python"]
}

result=json.dump(person_dict)
print(result)





