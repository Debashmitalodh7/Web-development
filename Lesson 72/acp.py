import tkinter as tk
from tkinter import messagebox

def calculate_product():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())

        product = num1 * num2

        result_label.config(text=f"Product = {product}")

    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter valid numbers")

window = tk.Tk()
window.title("Product Calculator")
window.geometry("400x300")

heading = tk.Label(window, text="Multiply Two Numbers", font=("Arial", 16))
heading.pack(pady=10)

label1 = tk.Label(window, text="Enter First Number:")
label1.pack()

entry1 = tk.Entry(window)
entry1.pack(pady=5)

label2 = tk.Label(window, text="Enter Second Number:")
label2.pack()

entry2 = tk.Entry(window)
entry2.pack(pady=5)

calculate_button = tk.Button(
    window,
    text="Calculate Product",
    command=calculate_product
)
calculate_button.pack(pady=15)

result_label = tk.Label(window, text="", font=("Arial", 14))
result_label.pack(pady=10)

window.mainloop()