from ClientModules.clientModules import *

def menu():
    print("\nMENU\n1 = Get Data\n2 = Update Data\n3 = New Data\n4 = Delete Data\n")



def main():
    # Initialize the program
    menu()
    choice = input("Key in your choice as per the menu : ")

    if choice not in ["1", "2", "3", "4"]:
        print("Error. Key in the right value as per the menu.")

    else:
        if choice == "1":
            query = "get:" + input("Key in country name : ").capitalize()
            print("Query : ", query)
            # results = ClientChat(query).messaging()
            print("Message recieved : ", ClientChat(query).messaging())

        elif choice == "2":
            pass

        elif choice == "3":
            pass

        elif choice == "4":
            pass

if __name__ == "__main__":
    main()
