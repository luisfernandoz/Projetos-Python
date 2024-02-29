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
        exit()
    else:
        print("Connected to the database\n")
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
                print("Event saved\n")
                break
            elif i == "2":
                print("Event not saved\n")
                break
            else:
                print("Invalid Option")
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
        print()
        main()

    elif a == "3":
        edit_event()

    elif a == "4":
        delete_event()

    elif a == "5":
        exit()

    elif a == "6":
        reset_all()
    else:
        print("\nInsert a Number between 1-5\n")
        main()


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
    id = input("Type the ID of the event you want to edit: ")
    print("What do you want to change?")
    print("(1) - Title")
    print("(2) - Description")
    print("(3) - Date")
    print("(4) - Back")
    opt = input("Type the option: ")


    if opt == "1":
        while True:
            upd_name = input("Type the new title: ")
            if len(upd_name) > 0:
                break
            else:
                print("Please insert a title")  
        sql = ("UPDATE eventos SET eve_nome = %s WHERE eve_id = %s ")
        values = (upd_name, id)
        mycursor.execute(sql, values)
        mydb.commit()
        print("Title has been changed")
        while True:
            aa = int(input("press 1 to edit an event, 2 to exit: "))
            if aa == 1:
                edit_event()
            elif aa == 2:
                main()
            else:
                print("Choose 1 or 2")


    elif opt == "2":
        while True:
            upd_desc = input("Type the new Description: ")
            if len(upd_desc) > 0:
                break
            else:
                print("Please insert a description.")
        sql = ("UPDATE eventos SET eve_desc = %s WHERE eve_id = %s ")
        values = (upd_desc, id)
        mycursor.execute(sql, values)
        mydb.commit()
        print("Description has been changed!")
        while True:
            aa = int(input("press 1 to edit an event, 2 to exit: "))
            if aa == 1:
                edit_event()
            elif aa == 2:
                main()
            else:
                print("Choose 1 or 2")

    elif opt == "3":
        while True:
            upd_date = input("Type the new Date (DD-MM-YYYY) (HH:MM): ")
            if len(upd_date) > 0:
                nw_date = datetime.datetime.strptime(upd_date, "%d-%m-%Y %H:%M")
                break
            else:
                print("Please insert a correct date.")
        sql = ("UPDATE eventos SET eve_date = %s WHERE eve_id = %s ")
        values = (nw_date, id)
        mycursor.execute(sql, values)
        mydb.commit()
        print("Date has been changed!")
        while True:
            aa = int(input("press 1 to edit an event, 2 to exit: "))
            if aa == 1:
                edit_event()
            elif aa == 2:
                main()
            else:
                print("Choose 1 or 2")

    elif opt == "4":
        main()

    else:
        print("please choose a number between 1 to 4.")
        edit_event()
    

def delete_event():
    id = input("Type the ID of the event you want to delete: ")
    sql = "DELETE FROM eventos WHERE eve_id = %s"
    val = (id, )
    i = input("Press 1 to delete or 2 to cancel: ")
    if i == "1":
        mycursor.execute(sql, val)
        mydb.commit()
        print("Event deleted\n")
        main()
    elif i == "2":
        print("Event not deleted\n")
        main()
    else:
        print("Invalid option")
        delete_event()
    
    main()

def reset_all():
    i = input("Press 1 to reset all events or 2 to cancel: ")
    if i == "1":
        mycursor.execute("DROP DATABASE calendario")
        mydb.commit()
        print("All events deleted")
        exit()
    elif i == "2":
        print("Events not deleted")
        main()
    else:
        print("Invalid option")
        reset_all()

main()

