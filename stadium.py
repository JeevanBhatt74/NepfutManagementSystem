import tkinter as tk
import sqlite3
import tkinter
from tkinter import messagebox
from tkinter import ttk
from PIL import Image, ImageTk
def add():
    window.destroy()
    import reg

# Import the ttk module for themed checkbox
window = tkinter.Tk()
window.title("Nepfut Management System")
window.iconbitmap("nep.ico")    
window.geometry("644x434")
window.config(bg="#f0f0f0")


#nepal logo
d=Image.open("stadium.jpg")
e=d.resize((800,400))
f=ImageTk.PhotoImage(e)
lbl1=tkinter.Label(image=f)
lbl1.place(x=515,y=-79) 
lbl1.grid(padx=300, pady=70)

su = tk.Label(window, text="", bg="#f0f0f0", fg="Black", font=("Microsoft YaHei UI", 16))

window.mainloop()