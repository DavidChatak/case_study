import json
def listele():
    with open("rehber.json") as file:
            rehber=json.load(file)
            print("#   Name\tLast-Name\tPhone_number")    
            for key in rehber:
                print(key,"--", rehber[key]["name"],"\t",rehber[key]["last_name"],"\t\t",rehber[key]["phone_number"])

while True:
    print("-----------------------")
    print(" 0  - list of  records")
    print(" 1  - new records")
    print(" 2  - modify record")
    print(" 3  - delete record")
    print("q/Q - Quit")
    print("-----------------------")
    opt=input("enter your choice:")
    if opt == "0": # listing 
        listele()        
    elif opt=="1":  #new record
        with open("rehber.json") as file:
            rehber=json.load(file)

        no = len(rehber)+1
        rehber[str(no)]={"name": "", "last_name": "", "phone_number": ""}
        rehber[str(no)]["name"] = input("Enter the Name:")
        rehber[str(no)]["last_name"] = input("Enter the Last_Name:")
        rehber[str(no)]["phone_number"] = input("Enter the phone_number:")
        with open("rehber.json","w") as file:
            j=json.dumps(rehber, indent=2)
            file.write(j)
            file.close()
    elif opt == "2": #modify 
        with open("rehber.json") as file:
            rehber=json.load(file)
        i = input("Enter the NAME to be modified:")
        for key in list(rehber):
            if rehber[key]["name"] == i.lower():
                rehber[key]["name"] = input("Enter the Name:")
                rehber[key]["last_name"] = input("Enter the Last_Name:")
                rehber[key]["phone_number"] = input("Enter the phone_number:")
        with open("rehber.json","w") as file:
            j=json.dumps(rehber, indent=2)
            file.write(j)
            file.close()

    elif opt == "3": #deleting...
        listele()
        with open("rehber.json") as file:
            rehber=json.load(file)
        i=input("enter # to delete...")
        for key in list(rehber):
            if key == str(i) :
                del rehber[key]
        
        with open("rehber.json","w") as file:
            j=json.dumps(rehber, indent=2)
            file.write(j)
            file.close()


        with open("rehber.json") as file:
            rehber=json.load(file)
        
        i=1
        yr={}
        for v in rehber.values():
            yr[str(i)] = v
            i+=1
        rehber = yr

        with open("rehber.json","w") as file:
            j=json.dumps(rehber, indent=2)
            file.write(j)
            file.close()
        
    elif opt.lower() == "q":
        break
    else:
        continue