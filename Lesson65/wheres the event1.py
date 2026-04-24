from tkinter import *
from tkinter import messagebox
window = Tk()
window.title('Event Handler')
window.geometry("100x100")

def handle_keypress(event):
    print(event.char)

window.bind("<Key>", handle_keypress)

def handle_click(event):
    print("\nThe button was clicked!")

button = Button(text="Click me!")
button.pack()

button.bind("<Button-1>", handle_click)

def hadle_name(event):
    print("\nHave a nice day")

button1 = Button(text="press me!")
button1.pack()

button1.bind("<Button-1>" , hadle_name)

def msg():
    messagebox.showwarning("Alert", "Stop! Virus Found.")

button2 = Button(window , text="Scan for virus" , command=msg)
button2.place(x=40, y=80)

window.mainloop()