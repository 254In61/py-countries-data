import mysql.connector
import json
import os


def mysql_query(query):
    # Establish a connection to the database
    connection = mysql.connector.connect(
            host="localhost",
            user=os.environ.get("MYSQL_SERVER_USER"),
            password=os.environ.get("MYSQL_SERVER_PASSWD"),
            database="mydb"
        )
    print('mysql_query() : Connected to MySQL database')

    cursor = connection.cursor()

    # Execute a query
    cursor.execute(query)
    output = cursor.fetchall() # Fetch results with cursor.fetchall()
    print("mysql_query() : Query results => ", output)

    cursor.close() # close the cursor and connection properly when you're done to avoid resource leaks.
    connection.close()
    print("mysql_query() : Connection to MYSQL closed") 

    return output

def string_output(query):
    
    # cursor.fetchall() returns output as a list 
    list_x = mysql_query(query)

    # Socket transmits in a string format so convert list to string
    # Server end will not process any data. Just querry the MySQL and send results through the socket.
    # Client to decide what to do with the end results.
    
    print("string_output() : Data string to client => ", json.dumps(list_x))
    
    return json.dumps(list_x)

class DBQuery():
    """
    - Job of class is just to interract with the MySQL DB Server.
    """
    def __init__(self,string_pattern):
        self.string_pattern = string_pattern
    
    def getData(self):
        query = "select * from Countries where CountryName = '{}'".format(self.string_pattern.split(":")[1])
        print("DBQuery().getData() => query : ", query)
        return string_output(query)
    
    def putData(self):
        pass

class ServerMessageExchange:
    """
    - Job of class is just to send and recieve messages from client through the created socket.
    """

    def __init__(self, clientsocket):
        self.clientsocket = clientsocket

    def messaging(self):
        """
        Step 1: Decode string pattern message recieved through clientsocket.
        Step 2: Based on the string pattern message, query the MySQL server.
        Step 3: Send query results back to client.
        """
        string_pattern = self.clientsocket.recv(1024).decode("utf-8")
        print("ServerMessageExchange().messaging() => string pattern : ", string_pattern)

        if "get" in string_pattern:
            self.clientsocket.sendall(DBQuery(string_pattern).getData().encode("utf-8"))

        elif "put" in string_pattern:
            self.clientsocket.sendall(DBQuery(string_pattern).putData().encode("utf-8"))

        # elif "post" in string_pattern:
        #     self.clientsocket.sendall(DataBase(string_pattern).postData().encode("utf-8"))

        # elif "delete" in string_pattern:
        #     self.clientsocket.sendall(DataBase(string_pattern).deleteData().encode("utf-8"))
