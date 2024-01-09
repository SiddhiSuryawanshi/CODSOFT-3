import tkinter as tk
from tkinter import ttk, messagebox
import random
import string

class PasswordGeneratorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Password Generator")
        
        self.style = ttk.Style()
        self.style.configure('TFrame', background='#363636')
        self.style.configure('TLabel', background='#363636', foreground='#FFFFFF', font=('Arial', 12))
        self.style.configure('TButton', background='#FFD700', foreground='#363636', font=('Arial', 12, 'bold'))
        self.style.configure('TEntry', background='#FFFFFF', font=('Arial', 12))

        self.frame = ttk.Frame(root, padding="20")
        self.frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

        self.label_length = ttk.Label(self.frame, text="Password Length:")
        self.label_length.grid(row=0, column=0, padx=10, pady=10, sticky="e")

        self.length_var = tk.StringVar()
        self.entry_length = ttk.Entry(self.frame, textvariable=self.length_var, width=5)
        self.entry_length.grid(row=0, column=1, padx=10, pady=10, sticky="w")

        self.label_result = ttk.Label(self.frame, text="Generated Password:")
        self.label_result.grid(row=1, column=0, padx=10, pady=10, sticky="e")

        self.result_var = tk.StringVar()
        self.entry_result = ttk.Entry(self.frame, textvariable=self.result_var, state="readonly", font=('Arial', 14, 'bold'))
        self.entry_result.grid(row=1, column=1, padx=10, pady=10, sticky="w")

        self.button_generate = ttk.Button(self.frame, text="Generate Password", command=self.generate_password)
        self.button_generate.grid(row=2, column=0, columnspan=2, pady=20)

    def generate_password(self):
        try:
            length = int(self.length_var.get())
            if length <= 0:
                messagebox.showerror("Error", "Please enter a valid password length.")
                return

            characters = string.ascii_letters + string.digits + string.punctuation
            password = ''.join(random.choice(characters) for _ in range(length))
            self.result_var.set(password)
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid number for the password length.")

def main():
    root = tk.Tk()
    app = PasswordGeneratorApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
