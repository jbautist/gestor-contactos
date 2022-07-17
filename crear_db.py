import db_connection as sql

sql.ddl('contactos.db',
'''CREATE TABLE datos_contactos (
  id_contacto INTEGER PRIMARY KEY AUTOINCREMENT,
  nombre TEXT,
  dirección TEXT,
  teléfono INTEGER,
  email TEXT
);
''')