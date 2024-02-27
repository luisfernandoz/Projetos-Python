@ -1,69 +0,0 @@
import datetime
import os

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
        print("Title: "+ new_title)
        print("Description: "+ description)
        format_date = date.strftime("%d-%m-%Y %H:%M")
        print("You entered:", format_date)
        input("Press 1 to save or 2 to cancel: ")
        if input == "1":
            save(new_title, description, date)
        elif input == "2":
            pass
    elif a == "2":
        print("\nAll Events: \n")
        print("Title, Description, Date")
        view_event()
    elif a == "3":
        edit_event()
    elif a == "4":
        delete_event()
    elif a == "5":
        exit()


def create_new_event():
    new_title = input("Insert title: ")
    description = input("Insert description: ")
    while True:
        nv_date = input("Insert date(DD-MM-YYYY HH:MM): ")
        try:
            date = datetime.datetime.strptime(nv_date, "%d-%m-%Y %H:%M")
            return new_title, description,date
        except ValueError:
            print("Please type in a valid date format (DD-MM-YYYY HH:MM)")

def view_event():
    f = open("save.txt", "r")
    i = 0
    for line in f:
        i+=1
        print("Event: "+str(i))
        print(line)

def edit_event():
    pass

def delete_event():
    pass

def save(a, b, c):
    with open("save.txt", "a") as file:
        file.write(a + ", " + b + ", " + c.strftime("%d-%m-%Y %H:%M") + "\n")

main()
