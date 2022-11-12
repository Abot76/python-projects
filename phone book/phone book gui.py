from tkinter import *
import os
  
root = Tk()
root.title("Phone book")
root.geometry('400x500')
  
# Information List
f_list = os.listdir() #preveri za kontakte ki obstajajo
f_list.remove("phone book gui.py")

def reset():
    Name.set("")
    Number.set("")
    Email.set("")

# Update Information
def update_book():
    select.delete(0,END)
    f_list = os.listdir() #preveri za kontakte ki obstajajo
    f_list.remove("phone book gui.py")
    for item in f_list:
        select.insert(END, item)

def view_info(n,p,e): #naredi novo okno kjer vidiš podatke kontakta
    n = n[::-1]
    n = n[4:]
    n = n[::-1]

    new_window=Toplevel()
    new_window.title(n+" info")
    new_window.geometry("300x100")

    n_label = Label(new_window, text="Name: "+n).pack(pady=3)
    p_label = Label(new_window, text="Number: "+p).pack(pady=3)
    e_label = Label(new_window, text="Email: "+e).pack(pady=3)
    
    close_button = Button(new_window, text="OK", command=new_window.destroy).pack(pady=3) #gumb da shraniš nov kontakt



# Add Information
def new():
    name = Name.get()
    tel_number = Number.get()
    email = Email.get()
    if name != "":
        if tel_number != "":
            if email != "":
                name = name + ".txt"
                with open(name,"w") as fp:
                    fp.write(tel_number)
                    fp.write("\n")
                    fp.write(email)
                    fp.close()
                    pass

                update_book()
                reset()
    
# View Information
def view():

    for i in select.curselection():
        selection = select.get(i)

    with open(selection,"r") as fp:
        contents = fp.readlines()
        fp.close()
        pass
    phone = contents[0]
    email = contents[1]
    view_info(selection,phone,email)

    print(selection)
  
# Delete Information
def delete():

    for i in select.curselection():
        selection = select.get(i)
    os.remove(selection)
    update_book()

# Add Buttons, Label, ListBox
Name = StringVar()
Number = StringVar()
Email = StringVar()

  

  
Label(root, text = 'Name').pack(pady=5)
Entry(root, textvariable = Name,width=50).pack(pady=10)
  
Label(root, text = 'Phone').pack(pady=5)
Entry(root, textvariable = Number,width=50).pack(pady=10)
  
Label(root, text = 'Email').pack(pady=5)
Entry(root, textvariable = Email,width=50).pack(pady=10)

  
Button(root,text="New",command=new).pack(pady=5)
Button(root,text="View",command=view).pack(pady=5)
Button(root,text="Delete",command=delete).pack(pady=5)
  


select = Listbox(root, height=12)
select.pack(pady=5)

#select.bind("<<ListboxSelect>>",update_select)
selection = select.get(ACTIVE)
print(selection)
update_book()

# Execute Tkinter
root.mainloop()