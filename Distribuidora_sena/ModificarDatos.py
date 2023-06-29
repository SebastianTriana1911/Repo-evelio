import mysql.connector
from conexion_singleton import ConexionSG

def modificarDatos ():
    conexion = ConexionSG.get_conexion("distribuidora_sena")
    cursor = conexion.cursor ()
    print("""
    1. primer_apellido
    2. segundo_apellido
    3. nombres
    4. correos
    """)
    opcion = input ("Que desea cambiar: ")
    codigo = int(input("Ingrese el codigo en el que se encuentra el dato que quiere modificar: "))
    cambio = input("Ingrese lo que desea modificarle al dato: ")
    match opcion:
        case "1":
            cursor.execute ("UPDATE clientes SET primer_apellido=%s WHERE codigo=%s", (cambio.upper(),codigo))
            conexion.commit ()
            return f"\n¡¡ Dato modificado con exito !!"
        case "2":
            cursor.execute ("UPDATE clientes SET segundo_apellido=%s WHERE codigo=%s", (cambio.upper(),codigo))
            conexion.commit ()
            return f"\n¡¡ Dato modificado con exito !!"
        case "3":
            cursor.execute ("UPDATE clientes SET nombres=%s WHERE codigo=%s", (cambio.upper(),codigo))
            conexion.commit ()
            return f"\n¡¡ Dato modificado con exito !!"
        case "4":
            cursor.execute ("UPDATE clientes SET correo=%s WHERE codigo=%s", (cambio,codigo))
            conexion.commit ()
            return f"\n¡¡ Dato modificado con exito !!"