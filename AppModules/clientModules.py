import socket

class ClientMessageExchange():
    """
    Class that handles chat.
    Gets input from CreateQuery class for the query to send.
    """
    def __init__(self,query,client_socket):
        self.query = query
        self.client_socket = client_socket
        
    def messaging(self):
        # Method to perform the messaging with server
        
        # Send query to server through socket
        self.client_socket.sendall(self.query.encode("utf-8"))

        # Recieve result from server
        query_result = self.client_socket.recv(1024).decode("utf-8")
        return query_result

class DataManager():
    # Class that handled get, put, update , delete
    def __init__(self,key):
        self.key = key

    def getData(self):
        return self.key + input("Key in country name : ").capitalize()

    def putData(self):
        return self.key + inputs_function()
    
    def postData(self):
        # Currently same as putData().. To be re-designed if needed.
        return self.key + inputs_function()
    
    def deleteData(self):
        return self.key + input("Key in country name : ").capitalize()


def perform_query(query):

    print("Query : ",query)

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((SERVER_HOST, PORT))

    return ClientMessageExchange(query,client_socket).messaging()

def menu():
    print("\nMENU\n1 = Get information\n2 = Put updated information\n3 = Post new information\n4 = Delete existing information\n")


def inputs_function():
    country = input("Key in country name : ")
    capital = input("Key in capitol name : ")
    leader  = input("Key in political leader full names : ")
    extras  = input("Any interesting fact about the country? : ")
    
    return country + ":"+ capital + ":" + leader + ":" + extras