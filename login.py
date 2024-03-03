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

#Nepfut logo
a=Image.open("abc.png")
b=a.resize((500,80))
c=ImageTk.PhotoImage(b)
lbl=tkinter.Label(image=c)
lbl.place(x=-15,y=-19) 
lbl.grid(padx=50, pady=70)

#nepal logo
d=Image.open("nep.png")
e=d.resize((220,250))
f=ImageTk.PhotoImage(e)
lbl1=tkinter.Label(image=f)
lbl1.place(x=-15,y=-79) 
lbl1.grid(padx=50, pady=70)

def toggle_password_visibility():
    password_entry.config(show="" if show_password_var.get() else "*")

def login():
    entered_username = username_entry.get()
    entered_password = password_entry.get()

    conn = sqlite3.connect("user_database.db")
    c = conn.cursor()

    # Retrieve the user from the database based on the entered username
    c.execute("SELECT * FROM users WHERE email=?", (entered_username,))
    user = c.fetchone()
    

    conn.close()

    if user and user[4] == entered_password:
        messagebox.showinfo(title="Login Success", message="You successfully logged in.")
        window.destroy()
        import interface
        
    

    else:
        messagebox.showerror(title="Login Failed", message="Invalid username or password")


frame = tk.Frame(bg="#f0f0f0")

# Creating widgets
login_label = tk.Label(
    frame, text="Login", bg="#f0f0f0", fg="#007FFF", font=("Microsoft YaHei UI Bold", 30)
)
username_label = tk.Label(
    frame, text="Username:   ", bg="#f0f0f0", fg="Black", font=("Microsoft YaHei UI", 16)
)

su = tk.Label(
    frame, text="Don't have an account sign up ?", bg="#f0f0f0", fg="Black", font=("Microsoft YaHei UI", 16)
)

username_entry = tk.Entry(frame, font=("Microsoft YaHei UI", 16))
username_entry.place(x=200, y=300)
password_entry = tk.Entry(frame, show="*", font=("Microsoft YaHei UI", 16))

password_label = tk.Label(
    frame, text="Password:   ", bg="#f0f0f0", fg="Black", font=("Microsoft YaHei UI", 16)
)

login_button = tk.Button(
    frame, text="Login", bg='#007FFF', fg='white', width=15, font=("Microsoft YaHei UI bold", 16),
    command=login  # Add the login command here
)
signup_button = tk.Button(
    frame, text="Sign up", bg='#007FFF', fg='white', width=15, font=("Microsoft YaHei UI bold", 12), command=add
)

# Show password checkbox
show_password_var = tk.BooleanVar()
show_password_checkbox = ttk.Checkbutton(
    frame,
    text="Show Password",
    variable=show_password_var,
    command=toggle_password_visibility,
    style="TCheckbutton",
)

# Placing widgets on the screen
username_label.grid(row=1, column=0)
login_label.grid(row=0, column=0, columnspan=2, sticky="news", pady=40)

username_entry.grid(row=1, column=1, pady=20)
su.place(x=40, y=450)
password_label.grid(row=2, column=0)
password_entry.grid(row=2, column=1, pady=20)

show_password_checkbox.grid(row=3, column=0, columnspan=2, pady=10)
login_button.grid(row=4, column=0, columnspan=2, pady=20)
signup_button.grid(row=5, column=0, columnspan=2, pady=100)

frame.place(x=900, y=80)

window.mainloop()
