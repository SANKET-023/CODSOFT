import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter import StringVar
import random
import string
import pyperclip

class PasswordGenerator:
    def __init__(self, root):
        self.root = root
        self.root.title("Password Generator")

       
        self.length_var = StringVar(value="12")
        self.use_lowercase_var = tk.BooleanVar(value=True)
        self.use_uppercase_var = tk.BooleanVar(value=True)
        self.use_digits_var = tk.BooleanVar(value=True)
        self.use_special_chars_var = tk.BooleanVar(value=True)

       
        self.create_widgets()

    def create_widgets(self):
       
        length_label = ttk.Label(self.root, text="Password Length:")
        length_entry = ttk.Entry(self.root, textvariable=self.length_var, width=5)

        
        use_lowercase_checkbox = ttk.Checkbutton(self.root, text="Lowercase", variable=self.use_lowercase_var)
        use_uppercase_checkbox = ttk.Checkbutton(self.root, text="Uppercase", variable=self.use_uppercase_var)
        use_digits_checkbox = ttk.Checkbutton(self.root, text="Digits", variable=self.use_digits_var)
        use_special_chars_checkbox = ttk.Checkbutton(self.root, text="Special Characters", variable=self.use_special_chars_var)

        
        generate_button = ttk.Button(self.root, text="Generate Password", command=self.generate_password)

        
        password_label = ttk.Label(self.root, text="Generated Password:")
        self.password_var = StringVar()
        password_entry = ttk.Entry(self.root, textvariable=self.password_var, state="readonly", width=30)

        
        copy_button = ttk.Button(self.root, text="Copy to Clipboard", command=self.copy_to_clipboard)

       
        length_label.grid(row=0, column=0, padx=20, pady=20)
        length_entry.grid(row=0, column=1, padx=20, pady=20)

        use_lowercase_checkbox.grid(row=1, column=0, padx=10, pady=5, sticky=tk.W)
        use_uppercase_checkbox.grid(row=2, column=0, padx=10, pady=5, sticky=tk.W)
        use_digits_checkbox.grid(row=3, column=0, padx=10, pady=5, sticky=tk.W)
        use_special_chars_checkbox.grid(row=4, column=0, padx=10, pady=5, sticky=tk.W)

        generate_button.grid(row=5, column=0, columnspan=2, pady=10)

        password_label.grid(row=6, column=0, padx=10, pady=5, sticky=tk.W)
        password_entry.grid(row=6, column=1, padx=10, pady=5, sticky=tk.W)
        
        copy_button.grid(row=7, column=0, columnspan=2, pady=10)

    def generate_password(self):
        try:
            length = int(self.length_var.get())
            use_lowercase = self.use_lowercase_var.get()
            use_uppercase = self.use_uppercase_var.get()
            use_digits = self.use_digits_var.get()
            use_special_chars = self.use_special_chars_var.get()

            if not any([use_lowercase, use_uppercase, use_digits, use_special_chars]):
                messagebox.showerror("Error", "Please select at least one character type.")
                return

            all_chars = ""
            if use_lowercase:
                all_chars += string.ascii_lowercase
            if use_uppercase:
                all_chars += string.ascii_uppercase
            if use_digits:
                all_chars += string.digits
            if use_special_chars:
                all_chars += string.punctuation

            password = ''.join(random.choice(all_chars) for _ in range(length))
            self.password_var.set(password)
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid password length.")

    def copy_to_clipboard(self):
        password = self.password_var.get()
        if password:
            pyperclip.copy(password)
            messagebox.showinfo("Copied", "Password copied to clipboard.")
        else:
            messagebox.showerror("Error", "Generate a password first.")

if __name__ == "__main__":
    root = tk.Tk()
    app = PasswordGenerator(root)
    root.mainloop()