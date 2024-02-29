import random


def rps():
    options = ["rock", "paper", "scissors"]

    w = 0
    l = 0
    tie = 0

    while True:
        user_input = input(
            "choose your options... Rock|Paper|Scissors or press Q to exit: ").lower()
        if user_input == "q":
            break
        if user_input not in options:
            print("please enter a valid option")
            continue
        computer_input = random.randint(0, 2)
        computer_input = options[computer_input]
        print("Computer choice: " + computer_input)
        if user_input == "rock" and computer_input == "scissors":
            w += 1
            print("You won!")
        elif user_input == "paper" and computer_input == "rock":
            w += 1
            print("You won!")
        elif user_input == "scissors" and computer_input == "paper":
            w += 1
            print("You won!")
        elif user_input == computer_input:
            tie += 1
            print("Tie!")
        else:
            l += 1
            print("You loose :C")

    print("Wins: " + str(w))
    print("Loses: " + str(l))
    print("Tie: " + str(tie))
    main()


def gtn():

    gtn_w = 0
    gtn_l = 0
    computer_number = random.randint(0, 10)
    while True:
        user_number = input(
            "Choose your number! Between 0 and 10 or press q to exit.")
        if str(user_number) == "q":
            break
        user_number = int(user_number)
        if user_number >= 11 or user_number <= -1:
            print("please enter a valid number")
            break
        if user_number == computer_number:
            print("You won! you guessed the number correctly!")
            gtn_w += 1
            computer_number = random.randint(0, 10)
        elif user_number < computer_number:
            print("The number is higher!")
            gtn_l += 1
        elif user_number > computer_number:
            print("The number is lower!")
            gtn_l += 1
    if (user_number == "q"):
        print("Wins: " + str(gtn_w))
        print("guesses: " + str(gtn_l))
        main()
    gtn()


def main():
    print("Choose your game: ")
    print("1. Rock, Paper, Scissors")
    print("2. Guess the number")
    print("3. quit")
    user_input = input("Enter your choice: ")
    if user_input == str(1):
        rps()
    elif user_input == str(2):
        gtn()
    elif user_input == str(3):
        print("Cya! Until next time")


main()
