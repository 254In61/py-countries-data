import mysql.connector
import json
import os

SERVER_HOST = '192.168.1.99' # Server's IP address..Can be resolved using gethostbyname() if using DNS.
PORT = 55556   # Arbitrary non-privileged port


def connect_mysql():
    return mysql.connector.connect( host = "localhost", user = os.environ.get('MYSQL_USER'),password = os.environ.get('MYSQL_PASSWORD'), database = "mydb")

class DataBase():
    """
    - A query comes in as a string value 'column_name:value_searched'
    - Query is split into the different values to fit into an sql WHERE format.
    - Results are converted into JSON string before returned.
    """
    def __init__(self,in_str):
        self.in_str = in_str

    def getData(self):

        try: 
            sql_con = connect_mysql()
            mycursor = sql_con.cursor()
 
            query = "select * from countries where country = '{}'".format(self.in_str.split(":")[1])
            print("Created MySQL Query : ",query)
            mycursor.execute(query)
            output = mycursor.fetchall() 
            print("Results from MySQL Server : ",mycursor.fetchall()) 

            if output == []:
                out_string = "ERROR.No data present"

            else:
                # mycursor.execute(query) returns a List
                # socket transmits a string, so List has to be converted to a string
                out_string = json.dumps(mycursor.fetchall()[0])
            
            print("Results sent to client : ",out_string)
            return out_string

        except IndexError:
            return "ERROR during data querry"
        except mysql.connector.errors.ProgrammingError:
            return "Unknown column in 'where clause'"
    
    def putData(self):
        pass

    def postData(self):
        pass

    def deleteData(self):
        pass

class ServerMessageExchange():
    """
    - Job of class is just to send and recieve messages from client through the created socket.
    """
    def __init__(self,clientsocket):
        self.clientsocket = clientsocket

    def messaging(self):
        """
        Step 1: Decode query message recieved through clientsocket.
        Step 2: Query the MySQL server through DataBaseQuery class
        Step 3: Send query results back to client.
        """
        query = self.clientsocket.recv(1024).decode("utf-8")
        print("Incoming Client message : ",query)

        if "get" in query:
            self.clientsocket.sendall(DataBase(query).getData().encode("utf-8"))

        elif "put" in query:
            self.clientsocket.sendall(DataBase(query).putData().encode("utf-8"))
        
        elif "post" in query:
            self.clientsocket.sendall(DataBase(query).postData().encode("utf-8"))
        
        elif "delete" in query:
            self.clientsocket.sendall(DataBase(query).deleteData().encode("utf-8"))
        
