from ClientModules.clientModules import *
import time


def main():
    # Continous testing of querrying.
    
    countries = ["Kenya","Uganda","USA","Rwanda","Tanzania","Indonesia"]

    for count in range(50):
        for country in countries:
            query = "get:" + country
            print("Message recieved : ", ClientChat(query).messaging())
        count += 1
        time.sleep(2)


if __name__ == "__main__":
    main()
