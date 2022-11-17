from tkinter import *

calculation = ""

def update_calculation(symbol):
    global calculation
    if symbol =="X":
        calculation= calculation[:-1]
    else:
        calculation += str(symbol)
    text_result.delete(1.0,"end")
    text_result.insert(1.0, calculation)

def calculate():
    global calculation
    try:
        calculation = str(eval(calculation))
        
        text_result.delete(1.0,"end")
        text_result.insert(1.0,calculation)

    except:
        clear_calculation()
        text_result.insert(1.0,"error")
        pass

def clear_calculation():
    global calculation
    calculation = ""
    text_result.delete(1.0,"end")




main = Tk()
main.geometry("230x275")
main.title("Calculator")
main.configure(bg="black")

buttonframe=Frame(main)
buttonframe.columnconfigure(1,weight=1)
buttonframe.columnconfigure(2,weight=1)
buttonframe.columnconfigure(3,weight=1)
buttonframe.columnconfigure(4,weight=1)
buttonframe.rowconfigure(1,weight=1)
buttonframe.rowconfigure(2,weight=1)
buttonframe.rowconfigure(3,weight=1)
buttonframe.rowconfigure(4,weight=1)
buttonframe.rowconfigure(5,weight=1)
buttonframe.rowconfigure(6,weight=1)
buttonframe.rowconfigure(7,weight=1)

text_result = Text(buttonframe, height=2, width=16,font=("Arial", 24),bg="black",fg="white")
text_result.grid(columnspan=5,sticky=NSEW)

text_buttonAC = Button(buttonframe, text="AC", command=clear_calculation, width=5,height=2, font=("Arial",17),bg="black",fg="#FF9C01")
text_buttonAC.grid(row=2, column=1,sticky=NSEW)

text_buttonDEL = Button(buttonframe, text="DEL", command=lambda: update_calculation("X"), width=5,height=15, font=("Arial",17),bg="black",fg="#FF9C01")
text_buttonDEL.grid(row=2, column=2,sticky=NSEW)

text_buttonMOD = Button(buttonframe, text="%", command=lambda: update_calculation("%"), width=5,height=15, font=("Arial",17),bg="black",fg="#FF9C01")
text_buttonMOD.grid(row=2, column=3,sticky=NSEW)

text_buttonDIV = Button(buttonframe, text="/", command=lambda: update_calculation("/"), width=5,height=15, font=("Arial",17),bg="black",fg="#FF9C01")
text_buttonDIV.grid(row=2, column=4,sticky=NSEW)

text_buttonMUL = Button(buttonframe, text="*", command=lambda: update_calculation("*"), width=5,height=15, font=("Arial",17),bg="black",fg="#FF9C01")
text_buttonMUL.grid(row=3, column=4,sticky=NSEW)

text_buttonADD = Button(buttonframe, text="+", command=lambda: update_calculation("+"), width=5,height=15, font=("Arial",17),bg="black",fg="#FF9C01")
text_buttonADD.grid(row=4, column=4,sticky=NSEW)

text_buttonSUB = Button(buttonframe, text="-", command=lambda: update_calculation("-"), width=5,height=15, font=("Arial",17),bg="black",fg="#FF9C01")
text_buttonSUB.grid(row=5, column=4,sticky=N+S+E+W)

text_buttonCAL = Button(buttonframe, text="=", command=calculate, width=5,height=15, font=("Arial",17),bg="#FF9C01",fg="white")
text_buttonCAL.grid(row=6, column=4,sticky=NSEW)
#Number buttons
text_button1 = Button(buttonframe, text="1", command=lambda: update_calculation(1), width=5,height=15, font=("Arial",17),bg="black",fg="white")
text_button1.grid(row=3, column=1,sticky=NSEW)

text_button2 = Button(buttonframe, text="2", command=lambda: update_calculation(2), width=5,height=15, font=("Arial",17),bg="black",fg="white")
text_button2.grid(row=3, column=2,sticky=NSEW)

text_button3 = Button(buttonframe, text="3", command=lambda: update_calculation(3), width=5,height=15, font=("Arial",17),bg="black",fg="white")
text_button3.grid(row=3, column=3,sticky=NSEW)

text_button4 = Button(buttonframe, text="4", command=lambda: update_calculation(4), width=5,height=15, font=("Arial",17),bg="black",fg="white")
text_button4.grid(row=4, column=1,sticky=NSEW)

text_button5 = Button(buttonframe, text="5", command=lambda: update_calculation(5), width=5,height=15, font=("Arial",17),bg="black",fg="white")
text_button5.grid(row=4, column=2,sticky=NSEW)

text_button6 = Button(buttonframe, text="6", command=lambda: update_calculation(6), width=5,height=15, font=("Arial",17),bg="black",fg="white")
text_button6.grid(row=4, column=3,sticky=NSEW)

text_button7 = Button(buttonframe, text="7", command=lambda: update_calculation(7), width=5,height=15, font=("Arial",17),bg="black",fg="white")
text_button7.grid(row=5, column=1,sticky=NSEW)

text_button8 = Button(buttonframe, text="8", command=lambda: update_calculation(8), width=5,height=15, font=("Arial",17),bg="black",fg="white")
text_button8.grid(row=5, column=2,sticky=NSEW)

text_button9 = Button(buttonframe, text="9", command=lambda: update_calculation(9), width=5,height=15, font=("Arial",17),bg="black",fg="white")
text_button9.grid(row=5, column=3,sticky=NSEW)

text_button0 = Button(buttonframe, text="0", command=lambda: update_calculation(0), width=12,height=15, font=("Arial",17),bg="black",fg="white")
text_button0.grid(row=6, column=1,columnspan=2,sticky=NSEW)

text_buttonPoint = Button(buttonframe, text=",", command=lambda: update_calculation("."), width=5,height=15, font=("Arial",17),bg="black",fg="white")
text_buttonPoint.grid(row=6, column=3,sticky=NSEW)

buttonframe.pack(fill="both")

main.mainloop()