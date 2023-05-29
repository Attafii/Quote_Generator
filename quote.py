from tkinter import messagebox
import tkinter as tk
import requests
from threading import Thread
import pyperclip


api=" http://api.quotable.io/random"
quotes=[]
quote_number=0
n=0
window= tk.Tk()
window.geometry("1100x500")
window.title("Quote Generator")
window.grid_columnconfigure(0, weight=1)
window.resizable(True,True)
window.configure(bg="grey")

def copy_text():
    pyperclip.copy(quotes[quote_number-1])
    tk.messagebox.showinfo("Success", "Text copied to clipboard!")


def Preload_Quotes():
    global quotes
    print("♪♪♪ Loading Quotes ♪♪♪")
    for x in range(10):
        random_quote= requests.get(api).json()
        content= random_quote["content"]
        author= random_quote["author"]
        quote=content + "\n\n" + "By " + author
        quotes.append(quote)
    
    
Preload_Quotes()



def get_random_quote():
    global quote_label
    global quotes
    global quote_number


    quote_label.configure(text=quotes[quote_number])
    quote_number= quote_number+1
    print(quote_number)
    if quotes[quote_number] == quotes[-3]:
        thread = Thread(target=Preload_Quotes)
        
        thread.start()

        


 

quote_label=tk.Label(window, text="Click on the button to generate a Quote",
                      height=9,
                      padx=15,
                      wraplength=900,
                      font=("Poppins",14))
quote_label.grid(row=0, column=0, stick="WE", padx=20, pady=10)
button = tk.Button(text="Generate", command=get_random_quote, bg='#66347F', fg='#ffffff', activebackground="#66347F", font=("Poppins",14))
button.grid(row=1, column=0, padx=5, pady=5)  
button = tk.Button(text="Copy text", command=copy_text, bg='#ffffff', fg='#66347F', activebackground="#ffffff", font=("Poppins",14))
button.grid(row=2, column=0, padx=10, pady=10) 




if __name__ == "__main__":
    window.mainloop()




 



