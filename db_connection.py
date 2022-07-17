import sqlite3


def ddl(database: str, instruccionsql: str):
    '''Ejecuta instrucciones SQL del tipo DDL.

    Args:
        database (str): Base de datos a realizar la consulta.
        instruccionsql (str): Comandos CREATE, ALTER, DROP.
    '''    

    connection = sqlite3.connect(database)
    cursor = connection.cursor()
    cursor.executescript(instruccionsql)
    connection.commit()
    connection.close()


def dml(database: str, instruccionsql: str, valores: tuple = None):
    '''Ejecuta instrucciones SQL del tipo DML.

    Args:
        database (str): Base de datos a realizar la consulta.
        instruccionsql (str): Comandos INSERT, UPDATE, DELETE.
        valores (tuple, optional): Valores a colocar en la instrucción. Defaults to None.
    '''   

    connection = sqlite3.connect(database)
    cursor = connection.cursor()
    cursor.execute(instruccionsql) if valores == None else cursor.execute(instruccionsql, valores)
    connection.commit()
    connection.close()


def dql(database: str, instruccionsql: str):
    '''Ejecuta instrucciones SQL del tipo DQL.

    Args:
        database (str): Base de datos a realizar la consulta.
        instruccionsql (str): Comandos SELECT.

    Returns:
        list: (tabla de resultados) con tuplas (registros).
    '''   

    connection = sqlite3.connect(database)
    cursor = connection.cursor()
    cursor.execute(instruccionsql)
    resultados = cursor.fetchall()
    connection.commit()
    connection.close()

    return resultados