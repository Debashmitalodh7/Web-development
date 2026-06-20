import tkinter as tk
import random

user_score = 0
computer_score = 0
rounds_played = 0

def play(user_choice):
    global user_score, computer_score, rounds_played

    choices = ["Rock", "Paper", "Scissors"]
    computer_choice = random.choice(choices)

    rounds_played += 1

    if user_choice == computer_choice:
        result = "It's a Tie!"
    elif (
        (user_choice == "Rock" and computer_choice == "Scissors")
        or (user_choice == "Paper" and computer_choice == "Rock")
        or (user_choice == "Scissors" and computer_choice == "Paper")
    ):
        result = "You Win!"
        user_score += 1
    else:
        result = "Computer Wins!"
        computer_score += 1

    result_label.config(
        text=f"Your Choice: {user_choice}\n"
             f"Computer Choice: {computer_choice}\n\n"
             f"{result}"
    )

    score_label.config(
        text=f"Your Score: {user_score}    Computer Score: {computer_score}"
    )

    rounds_label.config(text=f"Rounds Played: {rounds_played}")

def reset_game():
    global user_score, computer_score, rounds_played

    user_score = 0
    computer_score = 0
    rounds_played = 0

    result_label.config(text="Choose Rock, Paper, or Scissors")
    score_label.config(text="Your Score: 0    Computer Score: 0")
    rounds_label.config(text="Rounds Played: 0")


root = tk.Tk()
root.title("Rock Paper Scissors")
root.geometry("450x400")
root.configure(bg="lightblue")

heading = tk.Label(
    root,
    text="Rock Paper Scissors Game",
    font=("Arial", 18, "bold"),
    bg="lightblue"
)
heading.pack(pady=10)

result_label = tk.Label(
    root,
    text="Choose Rock, Paper, or Scissors",
    font=("Arial", 12),
    bg="lightblue"
)
result_label.pack(pady=20)

button_frame = tk.Frame(root, bg="lightblue")
button_frame.pack()

rock_btn = tk.Button(
    button_frame,
    text="Rock",
    width=12,
    command=lambda: play("Rock")
)
rock_btn.grid(row=0, column=0, padx=5)

paper_btn = tk.Button(
    button_frame,
    text="Paper",
    width=12,
    command=lambda: play("Paper")
)
paper_btn.grid(row=0, column=1, padx=5)

scissors_btn = tk.Button(
    button_frame,
    text="Scissors",
    width=12,
    command=lambda: play("Scissors")
)
scissors_btn.grid(row=0, column=2, padx=5)

score_label = tk.Label(
    root,
    text="Your Score: 0    Computer Score: 0",
    font=("Arial", 12, "bold"),
    bg="lightblue"
)
score_label.pack(pady=20)

rounds_label = tk.Label(
    root,
    text="Rounds Played: 0",
    font=("Arial", 12),
    bg="lightblue"
)
rounds_label.pack()

reset_btn = tk.Button(
    root,
    text="Reset Game",
    width=15,
    command=reset_game
)
reset_btn.pack(pady=20)

root.mainloop()