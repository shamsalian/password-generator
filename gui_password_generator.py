import tkinter as tk
from tkinter import messagebox
import secrets
import string

# Create Main Window
window = tk.Tk()
window.title("Password Generator")
window.geometry("500x500")
window.config(bg="lightblue")

# Title
title_label = tk.Label(
    window,
    text="Password Generator",
    font=("Arial", 22, "bold"),
    bg="lightblue",
    fg="black"
)

title_label.pack(pady=20)

# Password Length Label
length_label = tk.Label(
    window,
    text="Enter Password Length:",
    font=("Arial", 12),
    bg="lightblue"
)

length_label.pack()

# Password Length Entry
length_entry = tk.Entry(
    window,
    font=("Arial", 14),
    justify="center"
)

length_entry.pack(pady=10)

# Checkbox Variables
lower_var = tk.IntVar()
upper_var = tk.IntVar()
number_var = tk.IntVar()
symbol_var = tk.IntVar()

# Lowercase Checkbox
lower_check = tk.Checkbutton(
    window,
    text="Include Lowercase Letters",
    variable=lower_var,
    font=("Arial", 11),
    bg="lightblue"
)

lower_check.pack(pady=5)

# Uppercase Checkbox
upper_check = tk.Checkbutton(
    window,
    text="Include Uppercase Letters",
    variable=upper_var,
    font=("Arial", 11),
    bg="lightblue"
)

upper_check.pack(pady=5)

# Numbers Checkbox
number_check = tk.Checkbutton(
    window,
    text="Include Numbers",
    variable=number_var,
    font=("Arial", 11),
    bg="lightblue"
)

number_check.pack(pady=5)

# Symbols Checkbox
symbol_check = tk.Checkbutton(
    window,
    text="Include Symbols",
    variable=symbol_var,
    font=("Arial", 11),
    bg="lightblue"
)

symbol_check.pack(pady=5)

# Function to Generate Password
def generate_password():

    characters = ""

    # Add lowercase letters
    if lower_var.get() == 1:
        characters += string.ascii_lowercase

    # Add uppercase letters
    if upper_var.get() == 1:
        characters += string.ascii_uppercase

    # Add numbers
    if number_var.get() == 1:
        characters += string.digits

    # Add symbols
    if symbol_var.get() == 1:
        characters += string.punctuation

    # Validation
    if characters == "":
        messagebox.showerror(
            "Error",
            "Please select at least one option."
        )
        return

    # Get length
    try:
        length = int(length_entry.get())

        if length <= 0:
            messagebox.showerror(
                "Error",
                "Length must be greater than 0."
            )
            return

    except:
        messagebox.showerror(
            "Error",
            "Please enter a valid number."
        )
        return

    # Generate Password
    password = ""

    for i in range(length):
        password += secrets.choice(characters)

    # Show password
    password_entry.delete(0, tk.END)
    password_entry.insert(0, password)

# Generate Button
generate_button = tk.Button(
    window,
    text="Generate Password",
    font=("Arial", 12, "bold"),
    bg="green",
    fg="white",
    padx=10,
    pady=5,
    command=generate_password
)

generate_button.pack(pady=20)

# Password Output Box
password_entry = tk.Entry(
    window,
    font=("Arial", 14),
    width=30,
    justify="center"
)

password_entry.pack(pady=10)

# Copy Password Function
def copy_password():

    password = password_entry.get()

    if password == "":
        messagebox.showwarning(
            "Warning",
            "No password to copy."
        )
        return

    window.clipboard_clear()
    window.clipboard_append(password)

    messagebox.showinfo(
        "Copied",
        "Password copied to clipboard."
    )

# Copy Button
copy_button = tk.Button(
    window,
    text="Copy Password",
    font=("Arial", 12, "bold"),
    bg="blue",
    fg="white",
    padx=10,
    pady=5,
    command=copy_password
)

copy_button.pack(pady=10)

# Run Window
window.mainloop()