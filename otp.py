import tkinter as tk
import random
import string
import pyperclip

class PasswordGeneratorApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Password Generator")

        self.label_length = tk.Label(master, text="Password Length:")
        self.label_length.grid(row=0, column=0, padx=10, pady=10)

        self.entry_length = tk.Entry(master)
        self.entry_length.grid(row=0, column=1, padx=10, pady=10)

        self.generate_button = tk.Button(master, text="Generate Password", command=self.generate_password)
        self.generate_button.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

        self.copy_button = tk.Button(master, text="Copy to Clipboard", command=self.copy_to_clipboard)
        self.copy_button.grid(row=3, column=0, columnspan=2, padx=10, pady=10)
        self.copy_button.config(state=tk.DISABLED)

        self.password_label = tk.Label(master, text="")
        self.password_label.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

    def generate_password(self):
        try:
            length = int(self.entry_length.get())
            if length <= 0:
                raise ValueError("Password length must be a positive integer")
            
            characters = string.ascii_letters + string.digits + string.punctuation
            password = ''.join(random.choice(characters) for _ in range(length))
            self.password_label.config(text=password)
            self.copy_button.config(state=tk.NORMAL)
        except ValueError as e:
            self.password_label.config(text=str(e))
            self.copy_button.config(state=tk.DISABLED)

    def copy_to_clipboard(self):
        password = self.password_label.cget("text")
        pyperclip.copy(password)

def main():
    root = tk.Tk()
    app = PasswordGeneratorApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
