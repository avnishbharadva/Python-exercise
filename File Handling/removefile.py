import os

if os.path.exists("demotext.txt"):
    print("file exists")
    os.remove("demotext.txt")
else:
    print("File Not Found...")