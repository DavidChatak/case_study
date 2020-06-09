#!/usr/bin/python3
from os import system,name
# import sleep to show output for some time period 
from time import sleep 
  
# define our clear function 
def clear(): 
  
    # for windows 
    if name == 'nt': 
        _ = system('cls') 
  
    # for mac and linux(here, os.name is 'posix') 
    else: 
        _ = system('clear')
import sys
import json
def listele():
    with open("rehber.json") as file:
            rehber=json.load(file)
            print(f"{'#':<4}{'Name':<15}{'Last-Name':<15}{'Phone_number':<20}")    
            for key in rehber:
                print(f'{key:<2}--{rehber[key]["name"]:<15}{rehber[key]["last_name"]:<15}{rehber[key]["phone_number"]:<20}')

while True:
    print("-"*54)
    print("[ 0 ]  - list of  records")
    print("[ 1 ]  - new records")
    print("[ 2 ]  - modify record")
    print("[ 3 ]  - delete record")
    print("[q/Q] - Quit")
    print("-"*54)
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
        clear()
    elif opt == "2": #modify
        listele()
        with open("rehber.json") as file:
            rehber=json.load(file)
        i = str(input("Enter # to be modified:"))
        # for key in list(rehber):
        #     if rehber[key]["name"] == i.lower():
        #         rehber[key]["name"] = input("Enter the Name:")
        #         rehber[key]["last_name"] = input("Enter the Last_Name:")
        #         rehber[key]["phone_number"] = input("Enter the phone_number:")
        rehber[i]["name"] = input(f"change name of {rehber[i]['name']} as:")
        rehber[i]["last_name"] = input(f"change last_name of {rehber[i]['last_name']} as:")
        rehber[i]["phone_number"] = input(f"change phone_number of {rehber[i]['phone_number']} as:")
        
        with open("rehber.json","w") as file:
            j=json.dumps(rehber, indent=2)
            file.write(j)
            file.close()
        clear()

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
        clear()
        
    elif opt.lower() == "q":
        break
    else:
        continue
