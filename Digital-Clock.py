import tkinter as tk
from time import strftime

root = tk.Tk()
root.title("Digital Clock")
root.geometry("500x300")
root.resizable(True, True)

def time():
    string = strftime("%H:%M:%S %p\n%D")
    label.config(text=string)
    label.after(1000, time)

label = tk.Label(root, font=('Helvetica', 50, 'bold'), background='#2E3B4E', foreground='#FF5733', relief='solid', bd=10, padx=20, pady=20)
label.pack(expand=True, anchor='center', fill='both')

time()

root.mainloop()
