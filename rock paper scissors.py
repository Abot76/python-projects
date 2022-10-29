import random
winner = "tie"
choices = ["rock","paper","sissors"]

while winner == "tie":
    user_choice = input("what will you play as: ")

    comp_choice = random.choice(choices)
    if comp_choice == "rock":
        print("the computer chose rock")
    elif comp_choice == "paper":
        print("the computer chose paper")
    elif comp_choice == "scissors":
        print("the computer chose scissors")

    if user_choice == "rock":
        if comp_choice == "rock":
            print("tie!")
        elif comp_choice == "paper":
            winner = "computer"
        elif comp_choice == "scissors":
            winner = "user"

    elif user_choice == "paper":
        if comp_choice == "rock":
            winner = "user"
        elif comp_choice == "paper":
            print("tie!")
        elif comp_choice == "scissors":
            winner = "computer"

    elif user_choice == "scissors":
        if comp_choice == "rock":
            winner = "computer"
        elif comp_choice == "paper":
            winner = "user"
        elif comp_choice == "scissors":
            print("tie!")

if winner == "user":
    print("The user won!")

else:
    print("The computer won!")

