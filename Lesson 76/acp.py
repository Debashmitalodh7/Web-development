from tkinter import *
import random

choices = ["Rock", "Paper", "Scissors"]

def play(user_choice):
    computer_choice = random.choice(choices)

    user_label.config(text="You chose: " + user_choice)
    computer_label.config(text="Computer chose: " + computer_choice)

    if user_choice == computer_choice:
        result = "It's a Tie!"

    elif (user_choice == "Rock" and computer_choice == "Scissors") or \
         (user_choice == "Paper" and computer_choice == "Rock") or \
         (user_choice == "Scissors" and computer_choice == "Paper"):
        result = "You Win!"

    else:
        result = "Computer Wins!"

    result_label.config(text=result)

root = Tk()
root.title("Rock Paper Scissors Game")
root.geometry("450x350")
root.configure(bg="lightyellow")

heading = Label(root, text="Rock Paper Scissors",
                font=("Arial", 18, "bold"),
                bg="lightyellow")
heading.pack(pady=15)

instruction = Label(root, text="Choose Rock, Paper, or Scissors",
                    font=("Arial", 12),
                    bg="lightyellow")
instruction.pack()

button_frame = Frame(root, bg="lightyellow")
button_frame.pack(pady=20)

rock_button = Button(button_frame, text="Rock",
                     width=10, font=("Arial", 12, "bold"),
                     command=lambda: play("Rock"))
rock_button.grid(row=0, column=0, padx=10)

paper_button = Button(button_frame, text="Paper",
                      width=10, font=("Arial", 12, "bold"),
                      command=lambda: play("Paper"))
paper_button.grid(row=0, column=1, padx=10)

scissors_button = Button(button_frame, text="Scissors",
                         width=10, font=("Arial", 12, "bold"),
                         command=lambda: play("Scissors"))
scissors_button.grid(row=0, column=2, padx=10)

user_label = Label(root, text="",
                   font=("Arial", 12),
                   bg="lightyellow")
user_label.pack(pady=5)

computer_label = Label(root, text="",
                       font=("Arial", 12),
                       bg="lightyellow")
computer_label.pack(pady=5)

result_label = Label(root, text="",
                     font=("Arial", 16, "bold"),
                     fg="blue",
                     bg="lightyellow")
result_label.pack(pady=20)

root.mainloop()