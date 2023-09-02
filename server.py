# Server side script
import socket
import mysql.connector
import json
import os
from AppModules.server_modules import *

def main():
    print("Create the initial server socket .....")
    s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print("Binding socket....")
    s.bind((SERVER_HOST, PORT))
    print("Putting socket in listening state....")
    s.listen(1)

    # test_data()
    print("Get into while loop.....")
    while True:
        # Server socker role is just to create client socket & 
        # Client socket handles the exchange between client and server.
        print("\nListening for incoming connections...")
        (clientsocket, address) = s.accept()
        print('\nSuccessfull connection to : ', address)
        # messaging(clientsocket)
        Chat(clientsocket).messaging()

if __name__ == "__main__":
    main()

