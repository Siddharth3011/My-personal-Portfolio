import tkinter as tk
from tkinter import messagebox

# Backend logic
def click(event):
    global expression
    text = event.widget.cget("text")
    if text == "=":
        try:
            result = eval(expression)
            entry_var.set(result)
            expression = str(result)
        except Exception as e:
            messagebox.showerror("Error", "Invalid Expression")
            expression = ""
    elif text == "C":
        expression = ""
        entry_var.set("")
    else:
        expression += text
        entry_var.set(expression)

# Initialize the GUI
root = tk.Tk()
root.title("Calculator")
root.geometry("300x400")
root.resizable(False, False)

# Global variables
expression = ""
entry_var = tk.StringVar()

# Entry widget for displaying the expression/result
entry = tk.Entry(root, textvar=entry_var, font="Arial 20", justify="right", bg="#f4f4f4", bd=5, relief="groove")
entry.pack(fill="x", ipadx=8, pady=10, padx=10)

# Frame for buttons
button_frame = tk.Frame(root)
button_frame.pack()

# Button layout
buttons = [
    ['7', '8', '9', '/'],
    ['4', '5', '6', '*'],
    ['1', '2', '3', '-'],
    ['C', '0', '=', '+']
]

# Add buttons to the frame
for row in buttons:
    button_row = tk.Frame(button_frame)
    button_row.pack(fill="x")
    for button in row:
        btn = tk.Button(button_row, text=button, font="Arial 15", width=5, height=2, relief="ridge", bg="#e0e0e0")
        btn.pack(side="left", padx=5, pady=5)
        btn.bind("<Button-1>", click)

# Start the GUI main loop
root.mainloop()

