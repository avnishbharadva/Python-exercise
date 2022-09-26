import json

dictionary = {
    "name" : "Avnish Bharadva",
    "rollno" : 2,
    "number" : 9925184047,
    "city" : "Keshod",
    "dish" : "Dal Dhokli"
}

# with open("sample.json","w") as outfile:
#     json.dump(dictionary,outfile)

outfile = open("sample.json","w")
json.dump(dictionary,outfile)

print("Success !")