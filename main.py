# import tkinter
from tkinter import *

window=Tk()

window.title("day 27")
window.minsize(500,600)
label=Label(text="Alekhya",font=("Ariel",33,"bold"))
label.pack(expand=True)

input=Entry()
input.pack()

def clicky():
    # print(input.get())
    label.config(text=input.get())

button=Button(text="click",command=clicky)
button.pack()





window.mainloop()