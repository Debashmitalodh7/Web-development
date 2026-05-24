from tkinter import *
from tkinter import messagebox
import math

def calculate_interest():
    try:
        principal = float(entry_principal.get())
        rate = float(entry_rate.get())
        time = float(entry_time.get())

        simple_interest = (principal * rate * time) / 100

        compound_interest = principal * (math.pow((1 + rate / 100), time)) - principal

        result_si.config(text=f"Simple Interest = {simple_interest:.2f}")
        result_ci.config(text=f"Compound Interest = {compound_interest:.2f}")

    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter valid numbers.")

root = Tk()
root.title("Interest Calculator")
root.geometry("400x350")
root.configure(bg="lightblue")

heading = Label(root, text="Simple & Compound Interest Calculator",
                font=("Arial", 14, "bold"), bg="lightblue")
heading.pack(pady=10)

label_principal = Label(root, text="Principal Amount:", bg="lightblue",
                        font=("Arial", 11))
label_principal.pack()

entry_principal = Entry(root, width=25, font=("Arial", 11))
entry_principal.pack(pady=5)

label_rate = Label(root, text="Rate of Interest (%):", bg="lightblue",
                   font=("Arial", 11))
label_rate.pack()

entry_rate = Entry(root, width=25, font=("Arial", 11))
entry_rate.pack(pady=5)

label_time = Label(root, text="Time Period (Years):", bg="lightblue",
                   font=("Arial", 11))
label_time.pack()

entry_time = Entry(root, width=25, font=("Arial", 11))
entry_time.pack(pady=5)

calc_button = Button(root, text="Calculate",
                     font=("Arial", 12, "bold"),
                     bg="green", fg="white",
                     command=calculate_interest)
calc_button.pack(pady=15)

result_si = Label(root, text="", bg="lightblue",
                  font=("Arial", 12, "bold"))
result_si.pack(pady=5)

result_ci = Label(root, text="", bg="lightblue",
                  font=("Arial", 12, "bold"))
result_ci.pack(pady=5)

root.mainloop()