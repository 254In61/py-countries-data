# Module to connect to db
import mysql.connector
from mysql.connector import Error
import os

def query_db(sql_cmd):
    print("\n==> QUERY: ",sql_cmd)

    try:
        connection = mysql.connector.connect(
           host=os.environ.get("MYSQL_HOST"),
           user=os.environ.get("MYSQL_USER"),
           password=os.environ.get("MYSQL_PSWD"),
           database=os.environ.get("DB_NAME")
        )

        if connection.is_connected():
            print("\nConnected to MySQL Server")
            cursor = connection.cursor(dictionary=True)
            cursor.execute(sql_cmd)
        
            if sql_cmd == "select * from countries":
                print("\nQuerry results:\n")
                result = cursor.fetchall()
                print(result)
            else:
                print("\nQuerry results:\n")
                result = cursor.fetchone()
                print(result)

      
        cursor.close()
        connection.close()
        print("MySQL connection is closed")
        
        return result
    
    except Error as e:
        print("Error while connecting to MySQL", e)
        return "error"
