from tkinter import *
from datetime import date
window = Tk()
window.title("Getting started with Widights")
window.geometry("400x300")
lb1 = Label(text="Hey There! ", fg="white", bg= "#197A28", height=1, width = 20)
name_lb1 = Label(text="Full Name: ",bg = "#0E0EC8")
name_entry = Entry()
def display():
    name = name_entry.get()
    global Message
    message = "Welcome to the application \nToday's date is: "
    greet = "Hello " +name+ "\n"
    text_box.insert(END, greet)
    text_box.insert(END, message)
    text_box.insert(END, date.today())

text_box = Text(height = 3)
bth = Button(text = "begin", command = display, height = 1, bg = "#C80E11", fg = "yellow")
lb1.pack()
name_lb1.pack()
name_entry.pack()
bth.pack()
text_box.pack()
window.mainloop()


