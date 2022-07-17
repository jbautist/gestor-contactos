import os
import db_connection as sql


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
    ids_contactos = sql.dql('contactos.db', 'SELECT id_contacto FROM datos_contactos;')
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
    
    contactos = sql.dql('contactos.db', 'SELECT id_contacto, nombre FROM datos_contactos;')
    for tupla in contactos:
        id, nombre = tupla
        print(f'[{id}] {nombre}')


def ver():
    '''Muestra todos los valores de las columnas: 
    "nombre", "dirección", "teléfono" e "email" 
    de la tabla "datos_contactos"
    de la base de datos "contactos.db"
    ordenado alfabéticamente por "nombre".
    '''    

    datos = sql.dql('contactos.db', 'SELECT nombre, dirección, teléfono, email FROM datos_contactos ORDER BY nombre;')
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

        #Comprobando que el dato "telefono" ingresado sea válido.
        if not telefono.isnumeric():
            print('ERROR: ingresa un TELÉFONO válido.\n')
        else:
            break
    
    sql.dml('contactos.db',
    '''INSERT INTO datos_contactos (nombre, dirección, teléfono, email) 
    VALUES (?, ?, ?, ?);''', (nombre, direccion, telefono, email))
    
    print(f'El contacto {nombre} ha sido guardado.\n')


def editar():
    '''Modifica datos de la tabla "datos_contactos" 
    de la base de datos "contactos.db".
    
    1) Bucle while: el usuario indica el registro de editar.
    2) Bucle while: el usuario indica el campo de editar.
    3) Bucle while: el usuario ingresa el nuevo dato.
    '''

    ids = ids_contactos()
    if bool(ids) == False:
        print('No hay contactos guardados en la base de datos. Comience a agregar sus contactos con la opción "Agregar" del inicio.\n')
        return

    while True: 
        print('Ingrese el contacto a editar:\n')
        mostrar_nombres()
        print('\n[X] Cancelar\n')
        id_editar = input()
        clearConsole()
        if id_editar in ids:
            break
        elif id_editar.upper() == 'X':
            return
        else:
            print('ERROR: ingrese un contacto válido o ingrese [X] para cancelar la operación.\n')

    opciones = {'1': 'nombre',
                '2': 'dirección',
                '3': 'teléfono',
                '4': 'email'}
    while True: 
        print('''Indique el campo a editar:

    [1] NOMBRE
    [2] DIRECCIÓN
    [3] TELÉFONO
    [4] EMAIL

    [X] Cancelar
        ''')
        campo_editar = input()
        clearConsole()
        if campo_editar in opciones:
            break
        elif campo_editar.upper() == 'X':
            return
        else:
            print('ERROR: has ingresado un carácter o número inválido. Indique un campo del [1] al [4] o ingrese [X] para cancelar la operación.\n')

    while True:
        nuevo_valor = input('ingresa el nuevo dato: ')
        clearConsole()
        #Comprobando si el dato a modificar es "telefono", este valor ingresado sea válido.
        if campo_editar == '3':
            if not nuevo_valor.isnumeric():
                print('ERROR: ingresa un TELÉFONO válido.\n')
            else:
                break
        else:
            break
    
    nombre_editado = sql.dql('contactos.db', f'SELECT nombre FROM datos_contactos WHERE id_contacto = {id_editar};')
    sql.dml('contactos.db', f'UPDATE datos_contactos SET {opciones[campo_editar]} = "{nuevo_valor}" WHERE id_contacto = {id_editar};')

    print(f'El contacto {nombre_editado[0][0]} ha sido actualizado.\n')


def eliminar():
    '''Elimina registros de la tabla "datos_contactos"
    de la base de datos "contactos.db".'''
    
    ids = ids_contactos()
    if bool(ids) == False:
        print('No hay contactos guardados en la base de datos. Comience a agregar sus contactos con la opción "Agregar" del inicio.\n')
        return

    while True: 
        print('Ingrese el contacto a eliminar:\n')
        mostrar_nombres()
        print('\n[X] Cancelar\n')
        id_eliminar = input()
        clearConsole()
        if id_eliminar in ids:
            break
        elif id_eliminar.upper() == 'X':
            return
        else:
            print('ERROR: ingrese un contacto válido o ingrese [X] para cancelar la operación.\n')

    nombre_eliminado = sql.dql('contactos.db', f'SELECT nombre FROM datos_contactos WHERE id_contacto = {id_eliminar};')
    sql.dml('contactos.db', f'DELETE FROM datos_contactos WHERE id_contacto = {id_eliminar};')

    print(f'El contacto {nombre_eliminado[0][0]} ha sido eliminado.\n')