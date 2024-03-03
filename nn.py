import tkinter as tk
from tkinter import ttk

# Create the main application window
root = tk.Tk()
root.title("Treeview Example")
root.configure(bg="#1f446e")  # Set background color of the entire page

#heading
heading_label = tk.Label(root, text="PLAYER'S INFORMATION ",bd=10,relief="groove",bg="#1f446e", fg="white", font=("TIMES NEW ROMAN BOLD", 30))
heading_label.pack(side="top",fill="x",pady=10)

# Create the first Treeview widget
tree1 = ttk.Treeview(root)
tree1["columns"] = ("S.N","Name", "Age", "Market value", "Club", "Contact duration", "Goals", "Assists", "Preferred foot", "Position")

# Format column headings for the first table
tree1.heading("#0", text="S.N")
tree1.heading("#1", text="Name")
tree1.heading("#2", text="Age")
tree1.heading("#3", text="Market value")
tree1.heading("#4", text="Club")
tree1.heading("#5", text="Contact duration")
tree1.heading("#6", text="Goals")
tree1.heading("#7", text="Assists")
tree1.heading("#8", text="Preferred foot")
tree1.heading("#9", text="Position")

# Inserting data into the first table
# ... (your data insertion code for the first table)

# Inserting data into the Treeview
tree1.insert("", "end", text="1", values=("Kiran chemjong","33", "125k","Punjab fc","3 years","0", "0","Right","Goalkeeper"))
tree1.insert("", "end", text="2", values=("Deep karki","26", "75k","Birjung united","2 years","0", "0","Right","Goalkeeper"))
tree1.insert("", "end", text="3", values=("Sanish shrestha","23","125k","Lalitpur","3 years","0","0","Right","Defence"))
tree1.insert("", "end", text="4", values=("Rohit chand","32", "300k","Persik Kediri","4 years","0", "0","Right","Defence"))
tree1.insert("", "end", text="5", values=("Anjan rai","25", "100k","Chitwan FC","1 years","0", "0","Right","Defence"))
tree1.insert("", "end", text="6", values=("Armit shrestha","26", "75k","Jhapa FC","2 years","0", "0","Right","Defence"))
tree1.insert("", "end", text="7", values=("Arik Bista","23", "67k","Butwal FC","2 years","0", "0","Right","Defence"))
tree1.insert("", "end", text="8", values=("Chhiring Lama","21", "53.5k","Jhapa FC","8 months","1", "0","right","Defence"))
tree1.insert("", "end", text="9", values=("Yogesh gurung","21", "75k","Jhapa FC","1 years","0", "0","Left","Defence"))
tree1.insert("", "end", text="10", values=("laken limbu","21", "125k","Jhapa","1 years","0", "1","Right","Midfield"))
tree1.insert("", "end", text="11", values=("Utsav rai","20", "125k","Chitwan","2 years","0", "2","Right","Midfield"))
tree1.insert("", "end", text="12", values=("kritish ratna chunnju","22", "100k","Dhangadhi","3 years","1", "2","Right","Midfield"))
tree1.insert("", "end", text="13", values=("Manish dangi","22", "100k","rayong","1 years","4", "1","Right","Midfield"))
tree1.insert("", "end", text="14", values=("Seeshang aangdembe","23", "77k","lalitpur ","1 years","3", "2","right","Midfield"))
tree1.insert("", "end", text="15", values=("Nishan hamal","24", "54k","Nepzong","2 years","4", "3","Right","Midfield"))
tree1.insert("", "end", text="16", values=("Anjan bista","25", "175k","Jhapa fc","3 years","13", "2","Right","Forward"))
tree1.insert("", "end", text="17", values=("Ayush ghalan","20", "150k","Pokhara Thunder","1 years","3", "4","Left","Forward"))
tree1.insert("", "end", text="18", values=("Gillespye jung karki","25", "100k","Butwal lumbini","1 years","2", "1","Right","Forward"))
tree1.insert("", "end", text="19", values=("Rajesh pariyar","24", "75k","Chitwan","2 years","3", "0","Right","Forward"))
tree1.insert("", "end", text="20", values=("Hisub thapathaliya","25", "73.5k","Kathmandu Rayzers","6 months","1", "1","Left","Forward"))
tree1.insert("", "end", text="21", values=("Sanjeeb bista","24", "76k","Pokhara","9 months ","3", "2","Right","Forward"))
# Create the second Treeview widget
tree2 = ttk.Treeview(root)
tree2["columns"] = ("position","average age","market value","average market value")
tree1["height"]=21
# Format column headings for the second table
tree2.heading("#0", text="Postion")
tree2.heading("#1", text="Average Age")
tree2.heading("#2", text="Market value")
tree2.heading("#3", text="Average market value")
tree2.heading("#4", text="Average signing fee")


tree2.insert("", "end", text="Goal keeper", values=("27.33", "200k", "67k","37k"))
tree2.insert("", "end", text="Defence", values=("24.20", "450k", "90","43k"))
tree2.insert("", "end", text="Midfield", values=("23,29", "800k", "67k","67k"))
tree2.insert("", "end", text="Attack", values=("23.55", "875k", "109k","37k"))
# Place the Treeview widgets in the window
tree1.pack(padx=20, pady=40)
tree2.pack(padx=20, pady=40)
tree2["height"]=4

# Decrease the width of columns in the first Treeview
tree1.column("#0", width=80)  # S.N
tree1.column("#2", width=80)  # Age
tree1.column("#6", width=80)  # Goals
tree1.column("#7", width=80)  # Assists

# Set window size according to screen resolution
root.geometry("1920x1080")

# Start the Tkinter event loop
root.mainloop()
