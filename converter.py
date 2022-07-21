from tkinter import *

def miles_km():
    miles=float(miles_input.get())
    km =miles*1.6
    km_input.config(text=f"{km}")

window= Tk()
window.title("converter")
window.minsize(400,200)

miles_input=Entry()
miles_input.grid(column=1,row=0)
# miles_input.pack()

miles_label=Label(text="Miles")
miles_label.grid(column=2,row=0)

iet_label=Label(text="is equal to")
iet_label.grid(column=0,row=1)

km_input=Label(text=0)
km_input.grid(column=1,row=1)

km_label=Label(text="Km")
km_label.grid(column=2,row=1)

button=Button(text="calculate",command=miles_km)
button.grid(column=1,row=2)





window.mainloop()