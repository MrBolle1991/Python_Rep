from tkinter import *
import sqlite3
import bcrypt

root = Tk()
root.geometry("500x300")
root.title("Benutzerlogin")

frame = Frame(root)
frame.pack()

# Verbindung zur SQLite-Datenbank herstellen
conn = sqlite3.connect('user_data.db')
cursor = conn.cursor()

# Funktion zur Überprüfung des Passworts
def verify_password(stored_hashed_password, input_password):
    return bcrypt.checkpw(input_password.encode('utf-8'), stored_hashed_password)

# Funktion für den Login-Button-Klick
def button1_clicked():
    username = my_entry.get()
    password = my_entry2.get()

    # SQL-Befehl zur Abfrage von Benutzerdaten
    select_query = 'SELECT * FROM users WHERE username = ?;'
    cursor.execute(select_query, (username,))
    user_data = cursor.fetchone()

    if user_data:
        stored_hashed_password = user_data[2]  # Annahme: Passwort ist in der dritten Spalte (Index 2)

        # Überprüfe, ob das eingegebene Passwort mit dem in der Datenbank gespeicherten übereinstimmt
        if verify_password(stored_hashed_password, password):
            login_status_label.config(text="Login erfolgreich!", fg="green")
        else:
            login_status_label.config(text="Ungültige Anmeldeinformationen", fg="red")
    else:
        login_status_label.config(text="Benutzer nicht gefunden", fg="red")

# GUI-Elemente
my_entry = Entry(frame, width=20)
my_entry.insert(0, "Username")
my_entry.pack(padx=5, pady=5)

my_entry2 = Entry(frame, width=20)
my_entry2.insert(0, "Password")
my_entry2.pack(padx=5, pady=5)

button1 = Button(text="Login", command=button1_clicked)
button1.pack(padx=3, pady=3)

login_status_label = Label(root, text="", fg="black")
login_status_label.pack()

root.mainloop()

# Verbindung zur Datenbank schließen
conn.close()