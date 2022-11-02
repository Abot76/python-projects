import os


while True:
    action = input("action: ")

    if action == "new":
        name = input("name: ")
        name = name + ".txt"
        tel_number = input("enter a phone number: ")
        email = input("enter an email adress: ")

        with open(name,"w") as fp:
            fp.write(tel_number)
            fp.write("\n")
            fp.write(email)
            fp.close()
            pass

    elif action == "list":
        list = os.listdir()
        list.remove("contacts.py")
        
        print(list)

    elif action == "delete":
        name = input("name of the contact: ")
        name = name + ".txt"
        os.remove(name)

    elif action == "read":
        name = input("name of the contact: ")
        name = name + ".txt"
        with open(name,"r") as fp:
            contents = fp.readlines()
            fp.close()
            pass
        tel_number = contents[0]
        email = contents[1]
        print()
        print(tel_number)
        print(email)

    elif action == "edit":
        name = input("name of the contact: ")
        name = name + ".txt"
        with open(name,"r") as fp:
            contents = fp.readlines()
            fp.close()
            pass
        tel_number = contents[0]
        email = contents[1]

        while True:
            editable=input("what info do you want to change / [ save ]? [ phone ] or [ email ]: ")

            if editable == "phone":
                tel_number_tmp = input("enter new phone: ")
                print()

            elif editable == "email":
                email_tmp = input("enter new email: ")
                print()

            elif editable == "save":
                print(tel_number + "=>"+ tel_number_tmp)
                print()
                print(email + "=>"+ email_tmp)

                if input("confirm? [ Y / N ]: ") == "Y":
                    os.remove(name)
                    tel_number = tel_number_tmp
                    email = email_tmp
                    with open(name,"w") as fp:
                        fp.write(tel_number)
                        fp.write("\n")
                        fp.write(email)
                        fp.close()
                        pass
                
                    break

                else:
                    break

    elif action == "quit":
        quit()

    print()
    print()