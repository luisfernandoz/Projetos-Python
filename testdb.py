import mysql.connector

try: 
    mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "",
    database = "mydatabase"
)
except mysql.connector.Error as err:
        print(err)
else:
    print("Connected to the database")