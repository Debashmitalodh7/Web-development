from tkinter import *

window = Tk()

def handle_keypress(event):
    """Print the character
    associated to the key
    pressed"""
    print(event.char)

# Bind keypress event to
# handle_keypress()
window.bind("<Key>", handle_keypress)

window.mainloop()

from tkinter import *

window = Tk()
window.title("Greeting App")
window.geometry("200x150")

def show_message():
    label.config(text="Nice to meet you!")

button = Button(window, text="Click me!", command=show_message)
button.pack(pady=20)

label = Label(window, text="")
label.pack()

window.mainloop()

