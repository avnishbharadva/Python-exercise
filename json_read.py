import json

openfile = open("sample.json","r")

json_obj = json.load(openfile)

# print(json_obj)
# print(type(json_obj))

for i,j in json_obj.items():
    print(i,j)