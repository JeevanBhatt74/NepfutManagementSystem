from tkinter import *
from tkinter import messagebox
import sqlite3
from PIL import Image, ImageTk

def create_table():
    conn = sqlite3.connect("football_database.db")
    c = conn.cursor()
    try:
        c.execute("""CREATE TABLE IF NOT EXISTS players (
                        ID INTEGER PRIMARY KEY AUTOINCREMENT,
                        name TEXT,
                        position TEXT,
                        age INT,
                        salary REAL,
                        club TEXT
                    )""")
        conn.commit()
        print("Table created successfully.")
    except sqlite3.Error as e:
        print(f"Error creating table: {e}")
    finally:
        conn.close()

def add_player():
    name = entry_name.get()
    position = entry_position.get()
    age = entry_age.get()
    salary = entry_salary.get()
    club = entry_club.get()

    if not name or not position or not age or not salary or not club:
        messagebox.showerror("Error", "Please fill in all fields.")
        return

    try:
        age = int(age)
        salary = float(salary)
    except ValueError:
        messagebox.showerror("Error", "Please enter valid numeric values.")
        return

    conn = sqlite3.connect("football_database.db")
    c = conn.cursor()
    c.execute("INSERT INTO players(name, position, age, salary, club) VALUES (?, ?, ?, ?, ?)",
            (name, position, age, salary, club))
    conn.commit()
    conn.close()
    clear_entries()
    show_players()

def update_player():
    selected_id = entry_id.get()

    if not selected_id or not selected_id.isdigit():
        messagebox.showerror("Error", "Please enter a valid ID for update.")
        return

    selected_id = int(selected_id)

    name = entry_name.get()
    position = entry_position.get()
    age = entry_age.get()
    salary = entry_salary.get()
    club = entry_club.get()

    if not name or not position or not age or not salary or not club:
        messagebox.showerror("Error", "Please fill in all fields.")
        return

    try:
        age = int(age)
        salary = float(salary)
    except ValueError:
        messagebox.showerror("Error", "Please enter valid numeric values.")
        return

    conn = sqlite3.connect("football_database.db")
    c = conn.cursor()
    c.execute("UPDATE players SET name=?, position=?, age=?, salary=?, club=? WHERE ID=?",
            (name, position, age, salary, club, selected_id))
    conn.commit()
    conn.close()
    clear_entries()
    show_players()

def delete_player():
    selected_id = entry_id.get()

    if not selected_id or not selected_id.isdigit():
        messagebox.showerror("Error", "Please enter a valid ID for delete.")
        return

    selected_id = int(selected_id)

    conn = sqlite3.connect("football_database.db")
    c = conn.cursor()
    c.execute("DELETE FROM players WHERE ID=?", (selected_id,))
    conn.commit()
    conn.close()
    clear_entries()
    show_players()
def more():
    import nn
def clear_entries(): 
    entry_id.delete(0, END)
    entry_name.delete(0, END)
    entry_position.delete(0, END)
    entry_age.delete(0, END)
    entry_salary.delete(0, END)
    entry_club.delete(0, END)

def show_players():
    players_listbox.delete(0, END)
    conn = sqlite3.connect("football_database.db")
    c = conn.cursor()
    c.execute("SELECT * FROM players")
    players = c.fetchall()
    for player in players:
        players_listbox.insert(END, f"ID: {player[0]} , Name: {player[1]}, Position: {player[2]}, Age: {player[3]}, "
                                    f"Salary: {player[4]}, Club: {player[5]}")

    conn.close()

# GUI Setup
root = Tk()
root.title("Nepfut Management System")
#root.iconbitmap("nep.ico")
root.configure(bg="#1f446e")  # Set background color of the entire page

# Frame for photo
photo_frame = Frame(root, bg="#1f446e")
photo_frame.grid(row=0, column=0, columnspan=2, padx=20, pady=20)

# Load and display the resized image
image = Image.open("abc.png")
resized_image = image.resize((700, 120))
photo = ImageTk.PhotoImage(resized_image)
image_label = Label(photo_frame, image=photo, bg="#1f446e")  # Set background color of the photo frame
image_label.image = photo  # keep a reference to avoid garbage collection
image_label.grid(row=0, column=0, padx=10, pady=10)

# Frame for input widgets and buttons
input_button_frame = Frame(root, borderwidth=7, relief="groove", bg="#1f446e")
input_button_frame.grid(row=1, column=0, padx=(50, 40), pady=(20, 30), sticky="w")

# Labels and Entry Widgets
Label(input_button_frame, text="ID:", bg="#1f446e", fg="white", font=("Microsoft YaHei UI bold", 20)).grid(row=0, column=0, padx=10, pady=10, sticky="w")
entry_id = Entry(input_button_frame, font=("Microsoft YaHei UI ", 16))
entry_id.grid(row=0, column=1, padx=10, pady=10, sticky="w")

Label(input_button_frame, text="Name:", bg="#1f446e", fg="white", font=("Microsoft YaHei UI bold", 20)).grid(row=1, column=0, padx=10, pady=10, sticky="w")
entry_name = Entry(input_button_frame, font=("Microsoft YaHei UI ", 16))
entry_name.grid(row=1, column=1, padx=10, pady=10, sticky="w")

Label(input_button_frame, text="Position:", bg="#1f446e", fg="white", font=("Microsoft YaHei UI bold", 20)).grid(row=2, column=0, padx=10, pady=10, sticky="w")
entry_position = Entry(input_button_frame, font=("Microsoft YaHei UI ", 16))
entry_position.grid(row=2, column=1, padx=10, pady=10, sticky="w")

Label(input_button_frame, text="Age:", bg="#1f446e", fg="white", font=("Microsoft YaHei UI bold", 20)).grid(row=3, column=0, padx=10, pady=10, sticky="w")
entry_age = Entry(input_button_frame, font=("Microsoft YaHei UI ", 16))
entry_age.grid(row=3, column=1, padx=10, pady=10, sticky="w")

Label(input_button_frame, text="Salary:", bg="#1f446e", fg="white", font=("Microsoft YaHei UI bold", 20)).grid(row=4, column=0, padx=10, pady=10, sticky="w")
entry_salary = Entry(input_button_frame, font=("Microsoft YaHei UI ", 16))
entry_salary.grid(row=4, column=1, padx=10, pady=10, sticky="w")

Label(input_button_frame, text="Club:", bg="#1f446e", fg="white", font=("Microsoft YaHei UI bold", 20)).grid(row=5, column=0, padx=10, pady=10, sticky="w")
entry_club = Entry(input_button_frame, font=("Microsoft YaHei UI ", 16))
entry_club.grid(row=5, column=1, padx=10, pady=10, sticky="w")

# Buttons
Button(input_button_frame, text="Add Player", bg='#007FFF', fg='white', width=15, bd=7, relief=GROOVE, font=("Microsoft YaHei UI bold", 16), command=add_player).grid(row=6, column=0, padx=10, pady=20)
Button(input_button_frame, text="Update Player", bg='#007FFF', fg='white', width=15, bd=7, relief=GROOVE, font=("Microsoft YaHei UI bold", 16), command=update_player).grid(row=6, column=1, padx=10, pady=20)
Button(input_button_frame, text="Delete Player", bg='#007FFF', fg='white', width=15, bd=7, relief=GROOVE, font=("Microsoft YaHei UI bold", 16), command=delete_player).grid(row=7, column=0, padx=10, pady=10)
Button(input_button_frame, text="Show Players", bg='#007FFF', fg='white', width=15, bd=7, relief=GROOVE, font=("Microsoft YaHei UI bold", 16), command=show_players).grid(row=7, column=1, padx=10, pady=10)

#INFO BUTTOM
details_buttons=Button(root, text="Detailed information",bg='green', fg='white', width=20,bd=5,relief=GROOVE, font=("Microsoft YaHei UI bold", 16), command=more)
details_buttons.place(x=20,y=20)

# Listbox to display players
players_listbox = Listbox(root, width=120, height=30)
players_listbox.grid(row=1, column=1, padx=(120, 0), pady=20, sticky="nsew")  # Adjusted padx to move further to the right

# Create table if not exists
create_table()

root.mainloop()
