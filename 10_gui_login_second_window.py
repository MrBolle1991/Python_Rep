from tkinter import *
import sqlite3
import bcrypt

# Funktion, um das zweite Fenster in einem neuen Thread zu öffnen

def open_second_window():
    global second_root  # Um das zweite Fenster außerhalb der Funktion zugänglich zu machen
    second_root = Tk()
    second_root.geometry("800x500")
    second_root.title("Zweites Fenster")

    # Weitere Elemente für das zweite Fenster hinzufügen
    label = Label(second_root, text="Erfolgreich eingeloggt!", font=("Arial", 20))
    label.pack(padx=10, pady=10)

    def hide_label():
        label.pack_forget()  # Verstecke das Label

    # Verzögerung von 2000 Millisekunden (2 Sekunden) für das Ausblenden des Labels
    second_root.after(2000, hide_label)

    second_root.mainloop()  # Neue mainloop für das zweite Fenster


def on_login_success():
    root.destroy()  # Schließe das erste Fenster nach erfolgreichem Login

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
            on_login_success()  # Schließe das erste Fenster nach erfolgreichem Login
            open_second_window()  # Öffne das zweite Fenster in einem neuen Thread
        else:
            login_status_label.config(text="Ungültige Anmeldeinformationen", fg="red")
    else:
        login_status_label.config(text="Benutzer nicht gefunden", fg="red")

# GUI-Elemente
my_entry = Entry(frame, width=20)
my_entry.insert(0, "Username")
my_entry.pack(padx=5, pady=5)

my_entry2 = Entry(frame, width=20, show='*')  # Hier wird das Attribut show='*' hinzugefügt
my_entry2.insert(0, "Password")
my_entry2.pack(padx=5, pady=5)

button1 = Button(text="Login", command=button1_clicked)
button1.pack(padx=3, pady=3)

login_status_label = Label(root, text="", fg="black")
login_status_label.pack()

root.mainloop()

# Verbindung zur Datenbank schließen
conn.close()
