import socket
import json
from AppModules.client_modules import *


def main():

    # Initialize the program
    choice = "Y"
    
    while True:
      getData()
      choice = input("\nContinue with program? y/n : ").capitalize()

      if choice != "Y":
        print("\nProgram ended....\n")
        break
        
      
def menu():
    print("\nMENU\n1 = Search by country name\n2 = Search by country capital\n")

def getData():
    menu()
    choice = input("Key in search criteria as per the menu : ")

    if choice not in ["1","2"]:
        print("Error. Key in the right value as per the menu.")

    else:

        if choice == "1":
            column_id = "country"

        elif choice == "2":
            column_id = "capital"

        query = column_id + ":" + input("Key in value : ").capitalize()
        print(perform_query(query))

if __name__ == "__main__":
    main()
