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

    # Fetch results with cursor.fetchall() 
    print("mysql_query() : Query results => ", cursor.fetchall())


    list_x = cursor.fetchall()

    out_string = json.dumps(list_x)
    print("mysql_query() : Data string to client => ", out_string)
                
    cursor.close() # close the cursor and connection properly when you're done to avoid resource leaks.
    connection.close()
    print("mysql_query() : Connection to MYSQL closed")
    
    return out_string

    # cursor.fetchall() returns a List            
    # socket transmits a string, so List has to be converted to a string
    # if cursor.fetchall() == []:
    #     out_string = "Country data not present"

    # else:
    #     out_string = json.dumps(cursor.fetchall()[0])
                
    #     cursor.close() # close the cursor and connection properly when you're done to avoid resource leaks.
    #     connection.close()
    #     print("mysql_query() : Connection to MYSQL closed")

    # return out_string
        
    
        # if connection.is_connected():
        #     print('mysql_query() : Connected to MySQL database')

        #     cursor = connection.cursor()

        #     # Execute a query
        #     cursor.execute(query) 

        #     # Fetch results
        #     rows = cursor.fetchall() # cursor.fetchall() returns a List
        #     print("mysql_query() : Query results => ", rows)
                
        #     # socket transmits a string, so List has to be converted to a string
        #     if mysql_query(query) == []:
        #         out_string = "Country data not present"

        #     else:
        #         out_string = json.dumps(mysql_query(query)[0])
                
        #     # cursor.close() # close the cursor and connection properly when you're done to avoid resource leaks.
        #     # connection.close()

        #     return out_string
                
            
        #     # except mysql.connector.Error as e:
        #     #     print(f"mysql_query() : Error executing SQL query: {e}")
        #     #     return "Error executing SQL query"

        #     # finally:
        #     #     if 'cursor' in locals():
        #     #         cursor.close() # close the cursor and connection properly when you're done to avoid resource leaks.

   
    # except mysql.connector.Error as e:
    #     print(f"mysql_query() : Error connecting to MySQL database: {e}")
    #     return "Error connecting to MySQL database"
    
    # finally:
    #     if 'connection' in locals() and connection.is_connected():
    #         connection.close() #  close the cursor and connection properly when you're done to avoid resource leaks.
    #         print('mysql_query() : MySQL database connection closed')

class DBQuery():
    """
    - Job of class is just to interract with the MySQL DB Server.
    """
    def __init__(self,string_pattern):
        self.string_pattern = string_pattern
    
    def getData(self):
        query = "select * from Countries where CountryName = '{}'".format(self.string_pattern.split(":")[1])
        print("DBQuery().getData() => query : ", query)
        return mysql_query(query)
    
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
