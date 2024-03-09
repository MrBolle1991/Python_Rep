import sqlite3
import bcrypt

# Verbindung zur SQLite-Datenbank herstellen (wenn die Datei nicht vorhanden ist, wird sie automatisch erstellt)
conn = sqlite3.connect('user_data.db')

# Ein Cursor-Objekt erstellen, um SQL-Befehle auszuführen
cursor = conn.cursor()

# Hash-Funktion für Passwörter
def hash_password(password):
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

# Beispielbenutzerdaten
username = "Bolle"
password = "1Qay2Wsx!"

# Passwort hashen (statt des Klartext-Passworts in der Datenbank zu speichern)
hashed_password = hash_password(password)

# SQL-Befehl zum Einfügen von Benutzerdaten
insert_query = 'INSERT INTO users (username, password) VALUES (?, ?);'
cursor.execute(insert_query, (username, hashed_password))

# Änderungen speichern und Verbindung schließen
conn.commit()
conn.close()