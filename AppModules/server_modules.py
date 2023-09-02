import socket
import mysql.connector
import json
import os

SERVER_HOST = '192.168.1.99' # Server's IP address..Can be resolved using gethostbyname() if using DNS.
PORT = 55555   # Arbitrary non-privileged port


def connect_mysql():
    return mysql.connector.connect( "localhost", os.environ.get('MYSQL_USER'),os.environ.get('MYSQL_PASSWORD'),"mydb")

class DataBaseQuery():
    """
    - A query comes in as a string value 'column_name:value_searched'
    - Query is split into the different values to fit into an sql WHERE format.
    - Results are converted into JSON string before returned.
    """
    def __init__(self,in_str):
        self.in_str = in_str

    def process(self):

        try: 
            sql_con = connect_mysql()
            mycursor = sql_con.cursor()

            query = "select * from countries where {} = '{}'".format(self.in_str.split(":")[0],self.in_str.split(":")[1])
            print("Created MySQL Query : ",query)
            mycursor.execute(query)
            output = mycursor.fetchall()
            print("Results from MySQL Server : ",output)

            if output == []:
                out_string = "ERROR.No data present"

            else:
                out_string = json.dumps(output[0])
            
            print("Results sent to client : ",out_string)
            return out_string

        except IndexError:
            return "ERROR during data querry"

class Chat():
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
        query_result = DataBaseQuery(query).process()
        self.clientsocket.sendall(query_result.encode("utf-8"))

        return query_result

