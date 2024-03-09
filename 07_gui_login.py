from tkinter import *

#####

def button1_clicked():
    username = my_entry.get()
    password = my_entry2.get()

    if username == "Bolle" and password == "Password1337":
        login_status_label.config(text="Login Successful!", fg="green")
    else:
        login_status_label.config(text="Invalid credentials", fg="red")

#####

root = Tk()
root.geometry("500x300")
root.title("Benutzerlogin")

frame = Frame(root)
frame.pack()

my_entry = Entry(frame, width = 20)
my_entry.insert(0,"Username")
my_entry.pack(padx = 5, pady = 5)

my_entry2 = Entry(frame, width = 20)
my_entry2.insert(0,"Password")
my_entry2.pack(padx = 5,pady = 5)

Var1 = IntVar()
 
ChkBttn = Checkbutton(frame, text = "Eingeloggt bleiben", width = 15, variable = Var1)
ChkBttn.pack(padx = 5, pady = 5)

button1 = Button(text = "Login", command=button1_clicked)
button1.pack(padx = 3, pady = 3)

#####

login_status_label = Label(root, text="", fg="black")
login_status_label.pack()

#####

root.mainloop()