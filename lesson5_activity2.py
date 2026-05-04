from tkinter import *
from tkinter import messagebox
root = Tk()
root.title("Denomination Counter")
root.configure(bg="lightblue")
root.geometry("400x400")
lb1 = Label(
    root,
    text="Hey User! Welcome to the Domination Counter Application.",
    bg = "lightblue"
)
lb1.place (relx=0.5, y = 150, anchor = CENTER)
def msg():
    MsgBox = messagebox.showinfor(
        "Alert",
        "Do you want to calculate the demonination Count"
    )
    if MsgBox == "ok":
        topwin()
    button1 = Button(
        root, 
        text = "Lets get Started",
        command = msg,
        bg = "brown",
        fg = "white",
    )
    def topwin():
        top = Toplevel()
        top.title("Denomination Calculator")
        top.configure(bg = "light grey")
        top.geometry("500x600")
        label = Label(top, text= "Enter the amount", bg = "light grey")
        lb1 = Label(top, 
                    text = "Here are the number of notes for each demonination",
                    bg = "light grey")
        l1 = Label(top, text = "2000", bg = "light grey")
        l2 = Label(top, text = "500", bg = "light grey")
        l3 = Label(top, text = "100", bg = "light grey")

        t1 = Entry(top)
        t2 = Entry(top)
        t3 = Entry(top)

        def calculator():
            try:
                amount = int(entry.get())

                note2000 = amount // 2000
                amount %= 2000

                note500 = amount // 500
                amount %= 500
                
                note100 = amount // 100
                amount %= 100
                t1.delete(0, END)
                t1.insert(0, str(note2000))
                t2.delete(0, END)
                t2.insert(0, str(note500))
                t3.delete(0, END)
                t3.insert(0, str(note100))
            except ValueError:
                messagebox.showerror("Error", "Please enter a valid amount")
        btn = Button(
            top, 
            text = "Calculate",
            command = calculator,
            bg = "brown",
            fg = "white")
        label.place(x=230, y=50)
        entry.place(x=200, y = 80)
        btn.place(x=240, y=120)

        lb1.place(x=140,y = 170)
        l1.place(x = 180, y = 200)
        l2.place(x = 180, y = 230)
        l3.place(x = 180, y = 260)
        t1.place(x = 250, y = 200)
        t2.place(x = 250, y = 230)
        t3.place(x = 250, y = 260)
    
root.mainloop()
