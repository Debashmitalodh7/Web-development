from tkinter import *

window = Tk()

frame1 = Frame(master=window, width=100, height=100, bg="red")
frame1.pack(side=TOP)

frame2 = Frame(master=window, width=50, height=50, bg="yellow")
frame2.pack(side=LEFT)

frame3 = Frame(master=window, width=25, height=25, bg="blue")
frame3.pack(side=LEFT)

window = Tk()

label1 = Label(text="I'm at (0, 0)", bg="red")
label1.place(x=0, y=0)

label2 = Label(text="I'm at (75, 75)", bg="yellow")
label2.place(x=75, y=75)


window.mainloop()