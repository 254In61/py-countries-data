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
                cursor.execute(query) # cursor.execute(query) returns a List

                # Fetch results
                rows = cursor.fetchall()
                print("Query results : ", rows)
                return rows
            
            except mysql.connector.Error as e:
                print(f"Error executing SQL query: {e}")

            finally:
                if 'cursor' in locals():
                    cursor.close() # close the cursor and connection properly when you're done to avoid resource leaks.

   
    except mysql.connector.Error as e:
        print(f"Error connecting to MySQL database: {e}")
    
    finally:
        if 'connection' in locals() and connection.is_connected():
            connection.close() #  close the cursor and connection properly when you're done to avoid resource leaks.
            print('MySQL database connection closed')


class DataBase:
    """
    - A query comes in as a string value 'column_name:value_searched'
    - Query is split into the different values to fit into an sql WHERE format.
    - Results are converted into JSON string before returned.
    """

    def __init__(self, in_str):
        self.in_str = in_str

    def getData(self):
        
        query = "select * from Countries where CountryName = '{}'".format(self.in_str.split(":")[1])

        if mysql_query(query) == []:
            out_string = "ERROR.No data present"

        else:
            # socket transmits a string, so List has to be converted to a string
            out_string = json.dumps(mysql_query(query)[0])

            print("Results sent to client : ", out_string)
            return out_string

        # except IndexError:
        #     return "ERROR during data querry"
        
        # except mysql.connector.errors.ProgrammingError:
        #     return "Unknown column in 'where clause'"

    def putData(self):
        pass

    def postData(self):
        pass

    def deleteData(self):
        pass


class ServerMessageExchange:
    """
    - Job of class is just to send and recieve messages from client through the created socket.
    """

    def __init__(self, clientsocket):
        self.clientsocket = clientsocket

    def messaging(self):
        """
        Step 1: Decode query message recieved through clientsocket.
        Step 2: Query the MySQL server through DataBaseQuery class
        Step 3: Send query results back to client.
        """
        query = self.clientsocket.recv(1024).decode("utf-8")
        print("Incoming Client message : ", query)

        if "get" in query:
            self.clientsocket.sendall(DataBase(query).getData().encode("utf-8"))

        elif "put" in query:
            self.clientsocket.sendall(DataBase(query).putData().encode("utf-8"))

        elif "post" in query:
            self.clientsocket.sendall(DataBase(query).postData().encode("utf-8"))

        elif "delete" in query:
            self.clientsocket.sendall(DataBase(query).deleteData().encode("utf-8"))
