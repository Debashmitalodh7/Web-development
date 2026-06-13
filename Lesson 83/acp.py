import tkinter as tk
import random

def play(user_choice):
    choices = ["Rock", "Paper", "Scissors"]
    computer_choice = random.choice(choices)

    if user_choice == computer_choice:
        result = "It's a Tie!"
    elif (
        (user_choice == "Rock" and computer_choice == "Scissors") or
        (user_choice == "Paper" and computer_choice == "Rock") or
        (user_choice == "Scissors" and computer_choice == "Paper")
    ):
        result = "You Win!"
    else:
        result = "Computer Wins!"

    computer_label.config(text="Computer Chose: " + computer_choice)
    result_label.config(text=result)

window = tk.Tk()
window.title("Rock Paper Scissors")
window.geometry("500x400")
window.configure(bg="lightblue")

title_label = tk.Label(
    window,
    text="Rock Paper Scissors Game",
    font=("Arial", 18, "bold"),
    bg="lightblue"
)
title_label.pack(pady=20)

rock_button = tk.Button(
    window,
    text="Rock",
    font=("Arial", 14),
    width=10,
    command=lambda: play("Rock")
)
rock_button.pack(pady=5)

paper_button = tk.Button(
    window,
    text="Paper",
    font=("Arial", 14),
    width=10,
    command=lambda: play("Paper")
)
paper_button.pack(pady=5)

scissors_button = tk.Button(
    window,
    text="Scissors",
    font=("Arial", 14),
    width=10,
    command=lambda: play("Scissors")
)
scissors_button.pack(pady=5)

computer_label = tk.Label(
    window,
    text="Computer Chose: ",
    font=("Arial", 14),
    bg="lightblue"
)
computer_label.pack(pady=20)

result_label = tk.Label(
    window,
    text="",
    font=("Arial", 16, "bold"),
    bg="lightblue"
)
result_label.pack()

window.mainloop()