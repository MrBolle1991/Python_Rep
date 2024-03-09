from tkinter import *
import bcrypt

# Stored hashed password for user 'Bolle'
stored_hashed_password = b'$2b$12$qYWjpMVSWGEvOUlsLqo3dOGMDQ0S3ULPQpm2HjUSS6zsEEQOVHuL.'

# Function to verify the entered password
def verify_password(input_password):
    return bcrypt.checkpw(input_password.encode('utf-8'), stored_hashed_password)

# Function triggered on login button click
def button1_clicked():
    username = my_entry.get()
    password = my_entry2.get()

    if username == "Bolle" and verify_password(password):
        login_status_label.config(text="Login Successful!", fg="green")
    else:
        login_status_label.config(text="Invalid credentials", fg="red")

# Tkinter GUI code
root = Tk()
root.geometry("500x300")
root.title("User Login")

frame = Frame(root)
frame.pack()

my_entry = Entry(frame, width=20)
my_entry.insert(0, "Username")
my_entry.pack(padx=5, pady=5)

my_entry2 = Entry(frame, width=20)
my_entry2.insert(0, "Password")
my_entry2.pack(padx=5, pady=5)

Var1 = IntVar()
 
ChkBttn = Checkbutton(frame, text = "Eingeloggt bleiben", width = 15, variable = Var1)
ChkBttn.pack(padx = 5, pady = 5)

button1 = Button(text="Login", command=button1_clicked)
button1.pack(padx=3, pady=3)

login_status_label = Label(root, text="", fg="black")
login_status_label.pack()

root.mainloop()