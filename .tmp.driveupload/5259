import math
while True:
    repeat = 0
    correct = 0
    done = 0
    mode = input("What do you want to do? ")
    if mode == "add":
        first = input("First: ")
        second = input("Second: ")
        sum = float(first) + float(second)
        print("Sum: " + str(sum))
        done = 1

    elif mode == "subtract":
        first = input("First: ")
        second = input("Second: ")
        sum = float(first) - float(second)
        print("Sum: " + str(sum))
        done = 1

    elif mode == "multiply":
        first = input("First: ")
        second = input("Second: ")
        sum = float(first) * float(second)
        print("Sum: " + str(sum))
        done = 1


    elif mode == "divide":
        how = input("What do you want your result to be? (decimal/whole) ")
        if how == "decimal":
            first = input("First: ")
            second = input("Second: ")
            sum = float(first) / float(second)
            print("Sum: " + str(sum))
            done = 1

        elif how == "whole":
            first = float(input("First: "))
            second = float(input("Second: "))
            sum = math.floor(first / second)
            carry = first % second
            print("Sum: " + str(sum))
            print("Remains: " + str(carry))
            done = 1


    else:
        print("invalid operation")
        print("You can only add, subtract, multiply and divide.")
    if done == 1:

        while correct == 0:

            repeat = input("Do you want to do anything else? (True/False) ")

            if repeat == "True":
                correct = 1
                print("repeating...")

            elif repeat == "False":
                quit()
                correct = 1

            else:
                print("invalid answer")
                correct = 0
    else:
        print("repeating process...")