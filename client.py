import socket
import json
from AppModules.client_modules import *


def main():

    # Initialize the program
    choice = "Y"
    
    while True:
      dataHandler()
      choice = input("\nContinue with program? y/n : ").capitalize()

      if choice != "Y":
        print("\nProgram ended....\n")
        break
        
      

def dataHandler():
    menu()
    choice = input("Key in your choice as per the menu : ")

    if choice not in ["1","2","3" ,"4"]:
        print("Error. Key in the right value as per the menu.")

    else:
        if choice == "1":
            print(perform_query(DataManager.getData("get")))

        elif choice == "2":
            print(perform_query(DataManager.putData("put")))
        
        elif choice == "3":
            print(perform_query(DataManager.postData("post")))
        
        elif choice == "4":
            print(perform_query(DataManager.deleteData("delete")))

if __name__ == "__main__":
    main()
