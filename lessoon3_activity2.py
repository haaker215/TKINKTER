from tkinter import *
from tkinter import messagebox
root = Tk()
root.geometry("300x200")
def msg():
    messagebox.showwarning("Alert!, Stop! Virus Detected!")
    messagebox.showquestion("Do You want to repair/delete the virus?")
    messagebox.showerror("Acess Denied! You don't have permission to delete the virus!")
    messagebox.showinfo("IF you want to kepp the Accounts/personal info safe then plese format the drive and reinstall the OS!")

button = Button(root, text="Scan For Viruses", command=msg)
buttonq = Button(root, text="delete the virus", command=msg)
buttone = Button(root, text="Repair the virus", command=msg)
buttoni = Button(root, text  = "Format Device?", command=msg)
buttone.place(x = 40, y = 40)
button.place(x = 40, y = 80)
buttonq.place(x = 40, y = 120)
buttone.place(x = 40, y = 160)
buttoni.place(x = 40, y = 200)
root.mainloop()
