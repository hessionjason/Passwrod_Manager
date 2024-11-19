import hashlib
import tkinter as tk
from tkinter import messagebox, simpledialog

password_manager = {}

def create_account():
    username = simpledialog.askstring("Create Account", "Enter your desired username:")
    if username in password_manager:
        messagebox.showerror("Error", "Username already exists.")
        return
    password = simpledialog.askstring("Create Account", "Enter your desired password:", show="*")
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    password_manager[username] = hashed_password
    messagebox.showinfo("Success", "Account created successfully.")

def login():
    username = simpledialog.askstring("Login", "Enter your username:")
    password = simpledialog.askstring("Login", "Enter your password:", show="*")
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    if username in password_manager and password_manager[username] == hashed_password:
        messagebox.showinfo("Success", "Login successful.")
    else:
        messagebox.showerror("Error", "Incorrect username or password.")

def view_accounts():
    if password_manager:
        accounts = "\n".join(password_manager.keys())
        messagebox.showinfo("Accounts", f"List of accounts:\n{accounts}")
    else:
        messagebox.showinfo("Accounts", "No accounts have been created yet.")

def main_window():
    root = tk.Tk()
    root.title("Password Manager")

    tk.Label(root, text="Password Manager", font=("Arial", 16)).pack(pady=10)

    tk.Button(root, text="Create Account", command=create_account, width=20).pack(pady=5)
    tk.Button(root, text="Login", command=login, width=20).pack(pady=5)
    tk.Button(root, text="View Accounts", command=view_accounts, width=20).pack(pady=5)
    tk.Button(root, text="Exit", command=root.destroy, width=20).pack(pady=5)

    root.mainloop()

if __name__ == "__main__":
    main_window()
