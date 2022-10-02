f = open("demotext.txt","r")

content = f.readlines()

print(content)
print(type(content))

for i in content:
    print(i)

f.close()