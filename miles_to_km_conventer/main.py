from tkinter import *


def miles_to_km():
    miles = float(input.get())
    km = round(miles * 1.609)
    label3.config(text=f"{km}")
window = Tk()
window.minsize(width=300, height=200)
window.title("Miles To Km Conventer")
window.config(padx=20,pady=20)


input = Entry(width=7)
input.grid(column=1, row=0)

label = Label(text="Miles")
label.grid(column=2,row=0)

label1 = Label(text="is equal to")
label1.grid(column=0,row=1)

label3 = Label(text="0")
label3.grid(column=1,row=1)

label2 = Label(text="Km")
label2.grid(column=2,row=1)

#button

button = Button(text="Calculate",command=miles_to_km)
button.grid(column=1,row=2)

window.mainloop()