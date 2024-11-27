#Add libraries
import pymysql

#Create the function that we are goin to use later on.
def connect_mysql():
    try:
        # Establish the connection
        conexion = pymysql.connect(
            host="000.0.0.0",         # Change this if your MySQL server is elsewhere
            user="root",              # Replace with your username
            password="PASS",          # Replace with your password
            database="Database_name"  # Replace with the name of your database
        )
        print("Successful connection to the database")

        # Create a cursor to execute queries

    except pymysql.MySQLError as e:
        print("Error connecting to the database:", e)
        
    return conexion