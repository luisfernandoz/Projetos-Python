import datetime
import os

def main ():

    print("+-------------+")
    print("|Event manager|")
    print("+-------------+")
    print(" (1) - Create new event")
    print(" (2) - View event")
    print(" (3) - Edit event")
    print(" (4) - Delete event(s)")
    print(" (5) - Exit")

    a = input(" Choose an option: ")

    nv_title, date = create_new_event()

    print("Title: "+ str(nv_title))
    format_date = date.strftime("%d-%m-%Y %H:%M")
    print("You entered:", format_date)

    main()

def create_new_event():
    nv_title = input("Insert title: ")
    description = input("Insert description: ")
    while True:
        nv_date = input("Insert date(DD-MM-YYYY HH:MM): ")
        try:
            date = datetime.datetime.strptime(nv_date, "%d-%m-%Y %H:%M")
            save(nv_title, description, date)
            return nv_title, date
        except ValueError:
            print("Please type in Day, month and year.")

def save(a, b, c):
    with open("save.txt", "a") as file:
        file.write(a + "," + b + "," + c.strftime("%d-%m-%Y %H:%M") + "\n")

main()