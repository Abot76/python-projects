import random
winner = "tie"

while winner == "tie":
    user_choice = input("what will you play as: ")
    dice = random.randint(1,3)
    if dice == 1:
        comp_choice = "rock"
        print("The computer chose rock")
    elif dice == 2:
        comp_choice="paper"
        print("The computer chose paper")
    elif dice == 3:
        comp_choice = "scissors"
        print("The computer chose scissors")

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

