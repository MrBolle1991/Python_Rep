import sqlite3

# Verbindung zur SQLite-Datenbank herstellen (wenn die Datei nicht vorhanden ist, wird sie automatisch erstellt)
conn = sqlite3.connect('user_data.db')

# Ein Cursor-Objekt erstellen, um SQL-Befehle auszuführen
cursor = conn.cursor()

# SQL-Befehl zur Erstellung einer Benutzertabelle
create_table_query = '''
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL,
    password TEXT NOT NULL
);
'''

# Tabelle erstellen
cursor.execute(create_table_query)

# Änderungen speichern und Verbindung schließen
conn.commit()
conn.close()