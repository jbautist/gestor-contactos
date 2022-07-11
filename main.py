import os
import funciones 


clearConsole = lambda: os.system('cls' if os.name in ('nt', 'dos') else 'clear')


while True:
    print('''
    +----------------------------------+
    |            CONTACTOS             |
    +----------------------------------+

    Ingresa una opción:

    [1] Ver
    [2] Agregar
    [3] Editar
    [4] Eliminar

    [5] Salir
    ''')

    operacion = input()

    clearConsole()

    if operacion == '1':
        funciones.ver()
    elif operacion == '2':
        funciones.agregar()
    elif operacion == '3':
        funciones.editar()
    elif operacion == '4':
        funciones.eliminar()
    elif operacion == '5':
        exit()
    else:
        print('ERROR: has ingresado un carácter o número inválido. Por favor elige una operación del [1] al [4] o ingresa [5] para salir.')
        continue

    ENTER = input('[ENTER] Inicio')
    clearConsole()