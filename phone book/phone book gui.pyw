from tkinter import *
import os

# !!! THIS FILE NEEDS TO BE IN A SEPARATE FOLDER !!!

main_window = Tk()
main_window.title("Phone book")
main_window.geometry('171x250')
main_window.configure(bg="black")
  
# Information List
f_list = os.listdir() # Checks for contacts that already exist
f_list.remove("phone book gui.pyw")

# Updates Information
def update_book():
    select.delete(0,END)
    f_list = os.listdir() # Checks for contacts that already exist
    f_list.remove("phone book gui.pyw")

    for item in f_list:
        item = item.replace(".txt","")
        select.insert(END, item)

# Calls two specified functions
def sequence(*functions):
    def func(*args, **kwargs):
        return_value = None
        for function in functions:
            return_value = function(*args, **kwargs)
        return return_value
    return func

# Creates a new window where you can see the contact details
def view_info(n,p,e): 
    # Removes the ".txt" text at the end of the filename
    n = n[::-1]
    n = n[4:]
    n = n[::-1]

    view_window=Toplevel()
    view_window.title(n+" info")
    view_window.geometry("220x110")
    view_window.configure(bg="black")

    n_label = Label(view_window, text="Name: "+n, bg="black",fg="white").place(x=15,y=5)
    p_label = Label(view_window, text="Number: "+p, bg="black",fg="white").place(x=15,y=25)
    e_label = Label(view_window, text="Email: "+e, bg="black",fg="white").place(x=15,y=45)
    
    # Button to close the window
    close_button = Button(view_window, text="OK",width=7, command=view_window.destroy, bg="grey",fg="cyan").place(x=83,y=70)

# Function that saves the information into a text file
def save():
    global Name
    global Number
    global Email

    name = Name.get()
    tel_number = Number.get()
    email = Email.get()
    # Checks if all the fields have values entered
    if name != "":
        if tel_number != "":
            if email != "":

                # Creates the file and writes the information
                name = name + ".txt"
                with open(name,"w") as fp:
                    fp.write(tel_number)
                    fp.write("\n")
                    fp.write(email)
                    fp.close()
                    pass

                update_book()
                


# Create a new window where you enter information for a new contact
def new():
    global Name
    global Number
    global Email

    new_window=Toplevel()
    new_window.title("New contact")
    new_window.geometry("252x115")
    new_window.configure(bg="black")

    Name = StringVar()
    Number = StringVar()
    Email = StringVar()

    Label(new_window, text = 'Name', bg="black",fg="white").place(x=8,y=5)
    Entry(new_window, textvariable = Name,width=30, bg="grey",fg="white").place(x=55,y=5)
  
    Label(new_window, text = 'Phone', bg="black",fg="white").place(x=8,y=30)
    Entry(new_window, textvariable = Number,width=30, bg="grey",fg="white").place(x=55,y=30)
  
    Label(new_window, text = 'Email', bg="black",fg="white").place(x=8,y=55)
    Entry(new_window, textvariable = Email,width=30, bg="grey",fg="white").place(x=55,y=55)

    Button(new_window,text="Create",command=sequence(save,new_window.destroy), bg="grey",fg="lime").place(x=105,y=85)
    
# Function to get the information from a contact and pass it to another function that creates a window and displays it
def view():

    for i in select.curselection():
        selection = select.get(i)
        selection = selection + ".txt"

    with open(selection,"r") as fp:
        contents = fp.readlines()
        fp.close()
        pass
    phone = contents[0]
    email = contents[1]
    view_info(selection,phone,email)

  
# Function to delete a contact
def delete():

    for i in select.curselection():
        selection = select.get(i)
        selection = selection + ".txt"
    os.remove(selection)
    update_book()


# Buttons to create, delete and view contacts 
Button(main_window,text="New",command=new,fg="lime",bg="grey").place(x=8,y=5)
Button(main_window,text="View",command=view,fg="cyan",bg="grey").place(x=65,y=5)
Button(main_window,text="Delete",command=delete,fg="red",bg="grey").place(x=120,y=5)
  

# List of existing contacts
select = Listbox(main_window, height=12,width=25, bg="black",fg="white")
select.place(x=8,y=40)

selection = select.get(ACTIVE)
print(selection)
update_book()

main_window.mainloop()