import socket
from ServerModules.serverModules import *

# Server socker role is just to create client socket
# Client socket handles the exchange between client and server.

def main():
    print("Create the initial server socket .....")
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # Create an object out of socket class.

    print("Binding socket....")
    s.bind((os.environ.get("MYSQL_SERVER_HOST"), int(os.environ.get("MYSQL_SERVER_PORT"))))  # Using bind() method within the socket class.
    
    """
    The bind() method is used to associate a socket with a specific network interface and port number. 
     
    The bind() method typically requires a single argument, which is a tuple containing the IP address 
    and port number to bind the socket to. 
    
    Port has to be an integer
    
    Port has to be between 0-65535
    """
    print("Putting socket in listening state....")
    s.listen(1)  # Use listen() method within the socket class

    # test_data()
    print("Get into while loop.....")
    while True:
        print("\nListening for incoming connections...")
        (clientsocket, address) = s.accept()
        print("\nSuccessfull connection to : ", address)
        # messaging(clientsocket)
        ServerMessageExchange(clientsocket).messaging()


if __name__ == "__main__":
    main()
