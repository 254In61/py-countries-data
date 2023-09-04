# Server side script
import socket
from AppModules.server_modules import *

def main():
    print("Create the initial server socket .....")
    s=socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Create an object out of socket class.

    print("Binding socket....")
    s.bind((SERVER_HOST, PORT)) # Using bind() method within the socket class.

    print("Putting socket in listening state....") 
    s.listen(1) # Use listen() method within the socket class

    # test_data()
    print("Get into while loop.....")
    while True:
        # Server socker role is just to create client socket
        # Client socket handles the exchange between client and server.
        print("\nListening for incoming connections...")
        (clientsocket, address) = s.accept()
        print('\nSuccessfull connection to : ', address)
        # messaging(clientsocket)
        ServerMessageExchange(clientsocket).messaging()

if __name__ == "__main__":
    main()

