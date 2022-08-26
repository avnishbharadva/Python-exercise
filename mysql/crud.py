import crud_module as crm

# d = {'id' : 1,'name' : 'Avnish','City' : 'Keshod'}
# print(d["City"])
choice = -1

while choice!=0:
    print("\n1. Insert")
    print("2. Update")
    print("3. Delete")
    print("4. Get All Data")
    print("5. Search")
    print("0. Exit")
    choice = int(input("Enter Choice : "))

    if choice==1:
        sid = int(input("ID : "))
        name = input("Name : ")
        city = input("City : ")

        crm.insert(id=sid,name=name,city=city)
    if choice==2:
        sid = int(input("Enter Student Id for Update : "))
        name = input("Enter New Name : ")
        crm.update(sid,name)
    if choice==3:
        sid = int(input("Enter Student Id for Delete : "))
        crm.delete(sid)
    if choice==4:
        crm.get_all_data()
    if choice==5:
        sid = int(input("Enter Student Id : "))
        crm.search(sid)
    if choice==0:
        print("\nProgram Over")
        break