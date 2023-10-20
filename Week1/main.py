import tkinter as tk
from time import strftime

def time():
    string = strftime('%H:%M:%S %p')
    label.config(text=string)
    label.after(1000, time)

def date():
    string = strftime('%A, %B %d, %Y')
    date_label.config(text=string)

root = tk.Tk()
root.title("Digital Clock")

label = tk.Label(root, font=('calibri', 40, 'bold'), background='black', foreground='white')
label.pack(anchor='center')

date_label = tk.Label(root, font=('calibri', 18, 'bold'), background='black', foreground='white')
date_label.pack(anchor='center')

time()
date()

root.mainloop()
