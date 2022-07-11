import sqlite3 

connection = sqlite3.connect('contactos.db')
cursor = connection.cursor()
cursor.execute('''
CREATE TABLE datos_contactos (
  id_contacto INTEGER PRIMARY KEY AUTOINCREMENT,
  nombre TEXT,
  dirección TEXT,
  teléfono INTEGER,
  email TEXT
);
''')
connection.commit()
connection.close()