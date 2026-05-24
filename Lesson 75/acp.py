from tkinter import *

def check_strength():
    password = entry_password.get()
    length = len(password)

    if length == 0:
        result_label.config(text="Please enter a password", fg="red")

    elif length < 5:
        result_label.config(text="Weak Password", fg="red")

    elif 5 <= length < 8:
        result_label.config(text="Medium Password", fg="orange")

    else:
        result_label.config(text="Strong Password", fg="green")

root = Tk()
root.title("Password Strength Checker")
root.geometry("400x250")
root.configure(bg="lightblue")

heading = Label(root, text="Password Strength Checker",
                font=("Arial", 16, "bold"),
                bg="lightblue")
heading.pack(pady=15)

password_label = Label(root, text="Enter Password:",
                       font=("Arial", 12),
                       bg="lightblue")
password_label.pack()

entry_password = Entry(root, show="*", width=25,
                       font=("Arial", 12))
entry_password.pack(pady=10)

check_button = Button(root, text="Check Strength",
                      font=("Arial", 12, "bold"),
                      bg="blue", fg="white",
                      command=check_strength)
check_button.pack(pady=10)

result_label = Label(root, text="",
                     font=("Arial", 14, "bold"),
                     bg="lightblue")
result_label.pack(pady=15)

root.mainloop()