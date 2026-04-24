import tkinter as tk

# Function to convert inches to cm
def convert():
    try:
        inches = float(entry.get())
        cm = inches * 2.54
        result_label.config(text=f"Length in cm: {cm:.2f}")
    except ValueError:
        result_label.config(text="Please enter a valid number")

# Create main window
root = tk.Tk()
root.title("Inches to Centimeters Converter")
root.geometry("300x200")

# Input label
label = tk.Label(root, text="Enter length in inches:")
label.pack(pady=10)

# Entry box
entry = tk.Entry(root)
entry.pack(pady=5)

# Convert button
convert_button = tk.Button(root, text="Convert", command=convert)
convert_button.pack(pady=10)

# Result label
result_label = tk.Label(root, text="")
result_label.pack(pady=10)

# Run the app
root.mainloop()