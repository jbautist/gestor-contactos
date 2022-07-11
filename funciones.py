import os
import sqlite3


clearConsole = lambda: os.system('cls' if os.name in ('nt', 'dos') else 'clear')


def ids_contactos():
    '''Crea set con todos los valores de la columna "id_contacto" 
    de la tabla "datos_contactos"
    de la base de datos "contactos.db".

    Returns:
        set: Un set con strings de cada uno de los valores de la columna "id_contacto".
        Ejemplo:
        {'1', '3', '4', '6'}
    '''    

    ids = set()
    connection = sqlite3.connect('contactos.db')
    cursor = connection.cursor()
    cursor.execute('SELECT id_contacto FROM datos_contactos;')
    ids_contactos = cursor.fetchall()
    connection.commit()
    connection.close()

    for tupla in ids_contactos:
        for id in tupla:
            ids.add(str(id))
    return ids


def mostrar_nombres():
    '''Muestra todos los valores de las columnas: 
    "id_contacto" y "nombre" 
    de la tabla "datos_contactos"
    de la base de datos "contactos.db".
    '''

    connection = sqlite3.connect('contactos.db')
    cursor = connection.cursor()
    cursor.execute('SELECT id_contacto, nombre FROM datos_contactos;')
    contactos = cursor.fetchall()
    connection.commit()
    connection.close()

    for tupla in contactos:
        id, nombre = tupla
        print(f'[{id}] {nombre}')


def ver():
    '''Mustra todos los valores de las columnas: 
    "nombre", "dirección", "teléfono" e "email" 
    de la tabla "datos_contactos"
    de la base de datos "contactos.db"
    ordenado alfabéticamente por "nombre".
    '''    

    connection = sqlite3.connect('contactos.db')
    cursor = connection.cursor()
    cursor.execute('SELECT nombre, dirección, teléfono, email FROM datos_contactos ORDER BY nombre;')
    datos = cursor.fetchall()
    connection.commit()
    connection.close()

    for registro in datos:
        nombre, direccion, telefono, email = registro
        print(f'''
        NOMBRE: {nombre}
        DIRECCIÓN: {direccion}
        TELÉFONO: {telefono}
        EMAIL: {email}
        ''')


def agregar():
    '''Agrega nuevos registros en la tabla "datos_contactos" 
    de la base de datos "contactos.db".'''    

    while True: 
        print('Ingresa los campos del contacto:\n')
        nombre = input('NOMBRE: ')
        direccion = input('DIRECCIÓN: ')
        telefono = input('TELÉFONO: ')
        email = input('EMAIL: ')
        clearConsole()

        #Comprobando que los datos "nombre" y "teléfono" ingresados sean válidos.
        if not nombre.isalpha():
            print('ERROR: ingresa un NOMBRE válido.\n')
        elif not telefono.isnumeric():
            print('ERROR: ingresa un TELÉFONO válido.\n')
        else:
            break
    
    connection = sqlite3.connect('contactos.db')
    cursor = connection.cursor()
    cursor.execute('''INSERT INTO datos_contactos (nombre, dirección, teléfono, email) 
                        VALUES (?, ?, ?, ?);''', (nombre, direccion, telefono, email))
    connection.commit()
    connection.close()

    print(f'El contacto {nombre} ha sido guardado.\n')


def editar():
    '''Modifica datos de la tabla "datos_contactos" 
    de la base de datos "contactos.db".
    
    1) Bucle while: el usuario indica el registro de editar.
    2) Bucle while: el usuario indica el campo de editar.
    3) Bucle while: el usuario ingresa el nuevo dato.
    '''

    ids = ids_contactos()
    while True: 
        mostrar_nombres()
        id_editar = input('\nIngrese el contacto a editar: ')
        clearConsole()
        if id_editar in ids:
            break
        else:
            print('ERROR: ingrese un contacto válido.\n')

    opciones = {'1': 'nombre',
                '2': 'dirección',
                '3': 'teléfono',
                '4': 'email'}
    while True: 
        print('''
    Indique el campo a editar:

    [1] NOMBRE
    [2] DIRECCIÓN
    [3] TELÉFONO
    [4] EMAIL
        ''')
        campo_editar = input()
        clearConsole()
        if campo_editar in opciones:
            break
        else:
            print('ERROR: has ingresado un carácter o número inválido. Por favor indique un campo del [1] al [4].')

    while True:
        nuevo_valor = input('ingresa el nuevo dato: ')
        clearConsole()
        #Comprobando si los datos a modificar son "nombre" o "teléfono", estos valores ingresados sean válidos.
        if campo_editar == '1':
            if not nuevo_valor.isalpha():
                print('ERROR: ingresa un NOMBRE válido.\n')
            else:
                break
        elif campo_editar == '3':
            if not nuevo_valor.isnumeric():
                print('ERROR: ingresa un TELÉFONO válido.\n')
            else:
                break
        else:
            break

    connection = sqlite3.connect('contactos.db')
    cursor = connection.cursor()
    cursor.execute(f'SELECT nombre FROM datos_contactos WHERE id_contacto = {id_editar};')
    nombre_editado = cursor.fetchone()
    cursor.execute(f'UPDATE datos_contactos SET {opciones[campo_editar]} = "{nuevo_valor}" WHERE id_contacto = {id_editar};')
    connection.commit()
    connection.close()

    print(f'El contacto {nombre_editado[0]} ha sido actualizado.\n')


def eliminar():
    '''Elimina registros de la tabla "datos_contactos"
    de la base de datos "contactos.db".'''
    
    ids = ids_contactos()
    while True: 
        mostrar_nombres()
        id_eliminar = input('\nIngrese el contacto a eliminar: ')
        clearConsole()
        if id_eliminar in ids:
            break
        else:
            print('ERROR: ingrese un contacto válido.\n')

    connection = sqlite3.connect('contactos.db')
    cursor = connection.cursor()
    cursor.execute(f'SELECT nombre FROM datos_contactos WHERE id_contacto = {id_eliminar};')
    nombre_eliminado = cursor.fetchone()
    cursor.execute(f'DELETE FROM datos_contactos WHERE id_contacto = {id_eliminar};')
    connection.commit()
    connection.close()

    print(f'El contacto {nombre_eliminado[0]} ha sido eliminado.\n')