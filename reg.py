from tkinter import *
from tkinter import messagebox
import sqlite3

def create_table():
    conn = sqlite3.connect("user_database.db")
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS users (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    first_name TEXT,
                    last_name TEXT,
                    email TEXT,
                    password TEXT
                )''')
    conn.commit()
    conn.close()

def add_user():
    first_name = e1.get()
    last_name = e2.get()
    email = e3.get()
    password = e4.get()
    accepted_terms = checkbutt.get()  # Check if terms are accepted
    
    if not first_name or not last_name or not email or not password:
        messagebox.showerror("Error", "Please fill in all fields.")
        return
    if not accepted_terms:
        messagebox.showerror("Error", "Please confirm that you have accepted terms and privacy policy.")
        return
    
    conn = sqlite3.connect("user_database.db")
    c = conn.cursor()
    c.execute("INSERT INTO users (first_name, last_name, email, password) VALUES (?, ?, ?, ?)",
            (first_name, last_name, email, password))
    conn.commit()
    conn.close()

    messagebox.showinfo("Success", "User registered successfully!")

def go_to_login():
    reg.destroy()
    import login

reg = Tk()
reg.title("User Registration")
reg.geometry("1000x700")
reg.config(bg="#f0f0f0")

create_table()

# Labels
first_name = Label(reg, text='First name:', bg="#f0f0f0", fg="black", font=("Microsoft YaHei UI", 16))
secnd_name = Label(reg, text='Last name:', bg="#f0f0f0", fg="black", font=("Microsoft YaHei UI", 16))
email = Label(reg, text='Email:', bg="#f0f0f0", fg="black", font=("Microsoft YaHei UI", 16))
password = Label(reg, text='password:', bg="#f0f0f0", fg="black", font=("Microsoft YaHei UI", 16))
cpassword = Label(reg, text='Confirm password:', bg="#f0f0f0", fg="black", font=("Microsoft YaHei UI", 16))
first_name.place(x=625, y=180)
secnd_name.place(x=625, y=230)
email.place(x=625, y=280)
password.place(x=625, y=330)
cpassword.place(x=625, y=380)
h1 = Label(reg, text='Sign up', bg='#f0f0f0', fg="green", font=("Microsoft YaHei UI bold", 30))
h1.place(x=725, y=80)
e1 = Entry(reg, font=("Microsoft YaHei UI", 16))
e1.place(x=780, y=180)
e2 = Entry(reg, font=("Microsoft YaHei UI", 16))
e2.place(x=780, y=230)
e3 = Entry(reg, font=("Microsoft YaHei UI", 16))
e3.place(x=780, y=280)
e4 = Entry(reg, font=("Microsoft YaHei UI", 16), show='*')
e4.place(x=780, y=330)
e5 = Entry(reg, font=("Microsoft YaHei UI", 16), show='*')
e5.place(x=830, y=380)
des = Label(reg, text='I accept the term of use & privacy policy', bg="#f0f0f0", fg="black", font=("Microsoft YaHei UI", 12))
des.place(x=695, y=450)
checkbutt = BooleanVar()
checkbutt.set(False)
check_button = Checkbutton(reg, variable=checkbutt, bg="#f0f0f0")
check_button.place(x=670, y=450)

buton = Button(reg, text='Sign up', bg='green', fg='#f0f0f0', width=15, font=("Microsoft YaHei UI bold", 16), command=add_user)
buton.place(x=725, y=500)

goto = Label(reg, text='Already have an account go to login?', bg='#f0f0f0', fg="black", font=("Microsoft YaHei UI", 16))
goto.place(x=650, y=590)

btn = Button(reg, text="Go to Login", bg='green', fg='white', width=15, font=("Microsoft YaHei UI bold", 12), command=go_to_login)
btn.place(x=740, y=640)

reg.mainloop()
