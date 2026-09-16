import tkinter as tk
from tkinter import messagebox


# Login function
def login():
    username = username_entry.get()
    password = password_entry.get()

    # Demo credentials
    if username == "admin" and password == "1234":
        messagebox.showinfo("Login Successful", "Welcome, Admin!")
    else:
        messagebox.showerror("Login Failed", "Invalid username or password")


# Show / hide password
def toggle_password():
    if password_entry.cget("show") == "*":
        password_entry.config(show="")
        show_btn.config(text="Hide")
    else:
        password_entry.config(show="*")
        show_btn.config(text="Show")


# Main window
root = tk.Tk()
root.title("Login")
root.geometry("500x600")
root.resizable(False, False)
root.configure(bg="#f4f6f8")


# Login card
card = tk.Frame(
    root,
    bg="white",
    width=400,
    height=500
)
card.place(relx=0.5, rely=0.5, anchor="center")


# Title
title = tk.Label(
    card,
    text="Welcome Back!",
    font=("Arial", 26, "bold"),
    bg="white",
    fg="#222222"
)
title.pack(pady=(45, 5))


subtitle = tk.Label(
    card,
    text="Login to continue",
    font=("Arial", 11),
    bg="white",
    fg="#777777"
)
subtitle.pack(pady=(0, 30))


# Username label
username_label = tk.Label(
    card,
    text="Username",
    font=("Arial", 11, "bold"),
    bg="white",
    fg="#333333"
)
username_label.pack(anchor="w", padx=45)


# Username entry
username_entry = tk.Entry(
    card,
    font=("Arial", 12),
    width=32,
    relief="solid",
    bd=1
)
username_entry.pack(padx=45, pady=(8, 20), ipady=8)


# Password label
password_label = tk.Label(
    card,
    text="Password",
    font=("Arial", 11, "bold"),
    bg="white",
    fg="#333333"
)
password_label.pack(anchor="w", padx=45)


# Password frame
password_frame = tk.Frame(card, bg="white")
password_frame.pack(padx=45, pady=(8, 25))


# Password entry
password_entry = tk.Entry(
    password_frame,
    font=("Arial", 12),
    width=25,
    show="*",
    relief="solid",
    bd=1
)
password_entry.pack(side="left", ipady=8)


# Show password button
show_btn = tk.Button(
    password_frame,
    text="Show",
    command=toggle_password,
    bg="white",
    fg="#555555",
    relief="flat",
    cursor="hand2"
)
show_btn.pack(side="left", padx=5)


# Login button
login_btn = tk.Button(
    card,
    text="LOGIN",
    command=login,
    font=("Arial", 12, "bold"),
    bg="#2563eb",
    fg="white",
    activebackground="#1d4ed8",
    activeforeground="white",
    relief="flat",
    cursor="hand2",
    width=28,
    pady=10
)
login_btn.pack(pady=10)


# Forgot password
forgot = tk.Label(
    card,
    text="Forgot Password?",
    font=("Arial", 10),
    bg="white",
    fg="#2563eb",
    cursor="hand2"
)
forgot.pack(pady=15)


# Footer
footer = tk.Label(
    root,
    text="© 2026 Login System",
    font=("Arial", 9),
    bg="#f4f6f8",
    fg="#888888"
)
footer.pack(side="bottom", pady=15)


root.mainloop()