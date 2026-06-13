import tkinter as tk

window = tk.Tk()
window.configure(bg="lightgreen")

colors = [
    "#FFD1DC",  # Pastel Pink
    "#E0BBE4",  # Pastel Purple
    "#CDE7BE",  # Pastel Green
    "#FFFACD",  # Pastel Yellow
    "#B5EAD7",  # Pastel Mint
    "#C7CEEA",  # Pastel Blue
    "#FFDAC1",  # Pastel Peach
    "#D4F0F0",  # Pastel Cyan
    "#F3EAC2"   # Pastel Cream
]

color_index = 0

for i in range(3):
    for j in range(3):
        frame = tk.Frame(
            master=window,
            relief=tk.RAISED,
            borderwidth=1,
            bg="lightblue"
        )
        frame.grid(row=i, column=j, padx=5, pady=5)

        label = tk.Label(
            master=frame,
            text=f"Row {i}\nColumn {j}",
            bg=colors[color_index]
        )
        label.pack()

        color_index += 1

window.mainloop()