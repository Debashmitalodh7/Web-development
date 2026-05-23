# Tkinter App
# Takes Date of Birth as input
# Returns Present Age

import tkinter as tk
from tkinter import messagebox
from datetime import date

# Function to calculate age
def calculate_age():
    try:
        # Get input values
        day = int(day_entry.get())
        month = int(month_entry.get())
        year = int(year_entry.get())

        # Current date
        today = date.today()

        # Birth date
        birth_date = date(year, month, day)

        # Calculate age
        age = today.year - birth_date.year

        # Adjust if birthday has not occurred yet this year
        if (today.month, today.day) < (birth_date.month, birth_date.day):
            age -= 1

        # Display result
        result_label.config(text=f"Present Age: {age} years")

    except ValueError:
        messagebox.showerror(
            "Invalid Input",
            "Please enter a valid date"
        )

# Create main window
window = tk.Tk()
window.title("Age Calculator")
window.geometry("400x350")

# Heading
heading = tk.Label(
    window,
    text="Age Calculator",
    font=("Arial", 18)
)
heading.pack(pady=10)

# Day input
day_label = tk.Label(window, text="Enter Birth Day:")
day_label.pack()

day_entry = tk.Entry(window)
day_entry.pack(pady=5)

# Month input
month_label = tk.Label(window, text="Enter Birth Month:")
month_label.pack()

month_entry = tk.Entry(window)
month_entry.pack(pady=5)

# Year input
year_label = tk.Label(window, text="Enter Birth Year:")
year_label.pack()

year_entry = tk.Entry(window)
year_entry.pack(pady=5)

# Calculate button
calculate_button = tk.Button(
    window,
    text="Calculate Age",
    command=calculate_age
)
calculate_button.pack(pady=15)

# Result label
result_label = tk.Label(
    window,
    text="",
    font=("Arial", 14)
)
result_label.pack(pady=10)

# Run application
window.mainloop()