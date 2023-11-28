import mysql.connector
import json
import os


def mysql_query(query):
    # Establish a connection to the database
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user=os.environ.get("MYSQL_SERVER_USER"),
            password=os.environ.get("MYSQL_SERVER_PASSWD"),
            database="mydb"
        )
    
        if connection.is_connected():
            print('Connected to MySQL database')

            try:
                cursor = connection.cursor()

                # Execute a query
                cursor.execute(query) 

                # Fetch results
                rows = cursor.fetchall() # cursor.fetchall() returns a List
                print("Query results : ", rows)
                
                # socket transmits a string, so List has to be converted to a string
                if mysql_query(query) == []:
                    out_string = "Country data not present"

                else:
                    out_string = json.dumps(mysql_query(query)[0])

                return out_string
                
            
            except mysql.connector.Error as e:
                print(f"Error executing SQL query: {e}")
                return "Error executing SQL query"

            finally:
                if 'cursor' in locals():
                    cursor.close() # close the cursor and connection properly when you're done to avoid resource leaks.

   
    except mysql.connector.Error as e:
        print(f"Error connecting to MySQL database: {e}")
        return "Error connecting to MySQL database"
    
    finally:
        if 'connection' in locals() and connection.is_connected():
            connection.close() #  close the cursor and connection properly when you're done to avoid resource leaks.
            print('MySQL database connection closed')


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
        print("Incoming Client message : ", string_pattern)

        if "get" in string_pattern:
            query = "select * from Countries where CountryName = '{}'".format(string_pattern.split(":")[1])
            self.clientsocket.sendall(mysql_query(query).encode("utf-8"))

        elif "put" in string_pattern:
            self.clientsocket.sendall(mysql_query(query).encode("utf-8"))

        # elif "post" in string_pattern:
        #     self.clientsocket.sendall(DataBase(string_pattern).postData().encode("utf-8"))

        # elif "delete" in string_pattern:
        #     self.clientsocket.sendall(DataBase(string_pattern).deleteData().encode("utf-8"))
