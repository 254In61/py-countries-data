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
    
    # cursor.fetchall() returns output as a list enclosing a tuple
    list_x = mysql_query(query)

    # Socket transmits in a string format so convert list to string
    # End result is not a tuple within a list, but a sub-list within a list
    # Server end will not process any data. Just querry the MySQL and send results through the socket.
    # Client to decide what to do with the end results.
    
    print(json.dumps(list_x))
    
    return json.dumps(list_x)

class DBQuery():
    """
    - Job of class is just to interract with the MySQL DB Server.
    - Expects data in the format "<api action>:<Country name> e.g get:Kenya, post:Zambia, put:Australia, delete:USA
    """
    def __init__(self,string_pattern):
        self.string_pattern = string_pattern
    
    def getData(self):
        query = "select * from Countries where CountryName = '{}'".format(self.string_pattern.split(":")[1])
        print("DBQuery().getData() => query : ", query)
        return string_output(query)
    
    def putData(self):
        pass

