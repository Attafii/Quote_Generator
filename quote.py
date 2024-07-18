import tkinter as tk
from tkinter import messagebox
import pyperclip

quotes = [
    "The only way to do great work is to love what you do. - Steve Jobs",
    "Innovation distinguishes between a leader and a follower. - Steve Jobs",
    "Stay hungry, stay foolish. - Steve Jobs",
    "Your time is limited, don't waste it living someone else's life. - Steve Jobs",
    "Success is not final, failure is not fatal: It is the courage to continue that counts. - Winston Churchill",
    "The best way to predict the future is to create it. - Peter Drucker",
    "The only limit to our realization of tomorrow will be our doubts of today. - Franklin D. Roosevelt",
    "The future belongs to those who believe in the beauty of their dreams. - Eleanor Roosevelt"
]

quote_number = 0

def preload_quotes():
    global quotes
    print("♪♪♪ Loading Quotes ♪♪♪")
    # Replace this function with your own logic to populate the quotes list

def get_random_quote():
    global quote_number
    global quote_label
    if quote_number >= len(quotes):
        preload_quotes()
        quote_number = 0
    
    if quotes:
        quote_label.config(text=quotes[quote_number])
        quote_number += 1

def copy_text():
    global quote_number
    if quote_number > 0:
        try:
            pyperclip.copy(quotes[quote_number - 1])
            tk.messagebox.showinfo("Success", "Text copied to clipboard!")
        except IndexError:
            tk.messagebox.showerror("Error", "No quote to copy!")

window = tk.Tk()
window.geometry("1100x500")
window.title("Quote Generator")
window.grid_columnconfigure(0, weight=1)
window.resizable(True, True)
window.configure(bg="grey")

quote_label = tk.Label(window, text="Click on the button to generate a Quote",
                       height=9,
                       padx=15,
                       wraplength=900,
                       font=("Poppins", 14))
quote_label.grid(row=0, column=0, sticky="WE", padx=20, pady=10)

generate_button = tk.Button(window, text="Generate", command=get_random_quote,
                            bg='#66347F', fg='#ffffff', activebackground="#66347F",
                            font=("Poppins", 14))
generate_button.grid(row=1, column=0, padx=5, pady=5)

copy_button = tk.Button(window, text="Copy text", command=copy_text,
                        bg='#ffffff', fg='#66347F', activebackground="#ffffff",
                        font=("Poppins", 14))
copy_button.grid(row=2, column=0, padx=10, pady=10)

if __name__ == "__main__":
    preload_quotes()  # Preload quotes when starting the application
    window.mainloop()
