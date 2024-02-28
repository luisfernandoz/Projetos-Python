import datetime
import mysql.connector

def connect_to_database():
    try: 
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
        )
    except mysql.connector.Error as err:
        print(err)
        return None
    else:
        print("Connected to the database")
        return mydb

mydb = connect_to_database()
mycursor = mydb.cursor()
mycursor.execute("CREATE DATABASE IF NOT EXISTS calendario")
mycursor.execute("USE calendario")
mycursor.execute("CREATE TABLE IF NOT EXISTS eventos (eve_id INT AUTO_INCREMENT PRIMARY KEY, eve_nome VARCHAR(255), eve_desc TEXT, eve_date CHAR(16))")

def main ():
    
    print("+-------------+")
    print("|Event manager|")
    print("+-------------+")
    print(" (1) - Create new event")
    print(" (2) - View all event(s)")
    print(" (3) - Edit event")
    print(" (4) - Delete event(s)")
    print(" (5) - Exit")

    a = input(" Choose an option: ")

    if a == "1":
        new_title, description, date = create_new_event()
        
        while True:
            i = input("Press 1 to save or 2 to cancel: ")
            if i == "1":
                mycursor.execute("INSERT INTO eventos (eve_nome, eve_desc, eve_date) VALUES (%s, %s, %s)", (new_title, description, date))
                mydb.commit()
                print("Event saved")
                break
            elif i == "2":
                print("Event not saved")
                break
            else:
                print("Invalid option")
        main()

    elif a == "2":
        print("\nAll Events: \n")
        print("+----+-------+-------------+------+")
        print("| ID | Title | Description | Date |")
        print("+----+-------+-------------+------+")
        mycursor.execute("SELECT * FROM eventos ORDER BY eve_date ASC")
        result = mycursor.fetchall()

        for row in result:
            print(row)
        main()

    elif a == "3":
        edit_event()

    elif a == "4":
        delete_event()

    elif a == "5":
        exit()


def create_new_event():
    while True: 
        new_title = input("Insert title: ")
        if len(new_title) > 0:
            break
        else:
            print("Please insert a title")            
    description = input("Insert description: ")
    while True:
        nv_date = input("Insert date(DD-MM-YYYY HH:MM): ")
        try:
            date = datetime.datetime.strptime(nv_date, "%d-%m-%Y %H:%M")
            return new_title, description, date
        except ValueError:
            print("Please type in a valid date format (DD-MM-YYYY HH:MM)")

def edit_event():
    pass

def delete_event():
    pass



main()

