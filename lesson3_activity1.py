from tkinter import *
window = Tk()
window.title("Event Handling")
window.geometry("300x200")
def handle_keypress(event):
    print("Key pressed: ", event.char)
window.bind("<KeyPress>", handle_keypress)
def handle_click(event):
    print("\nThe Button was clicked!")
button = Button(window, text="Click Me!")
button.pack()
button.bind("<Button-1>", handle_click)
window.mainloop()