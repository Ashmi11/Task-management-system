import tkinter as tk
from task_manager_gui import TaskManagerGUI, TaskManager
from tkinter import Entry, Label, Button, messagebox


class LoginWindow:
    def __init__(self, root):
        self.root = root
        self.root.title("Login")

        self.username_label = tk.Label(root, text="Username:")
        self.username_label.pack()

        self.username_entry = tk.Entry(root)
        self.username_entry.pack()

        self.password_label = tk.Label(root, text="Password:")
        self.password_label.pack()

        self.password_entry = tk.Entry(root, show="*")
        self.password_entry.pack()

        self.login_button = tk.Button(root, text="Login", command=self.login)
        self.login_button.pack()

    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        # Replace with your own authentication logic
        if self.authenticate(username, password):
            self.root.destroy()
            self.launch_app()
        else:
            messagebox.showerror("Authentication Failed", "Invalid username or password. Try again.")

    def authenticate(self, username, password):
        # Replace with your own authentication logic
        return username == "admin" and password == "admin"

    def launch_app(self):
        root = tk.Tk()
        app = TaskManagerGUI(root)
        root.mainloop()


if __name__ == '__main__':
    login_root = tk.Tk()
    login_app = LoginWindow(login_root)

    login_root.mainloop()
