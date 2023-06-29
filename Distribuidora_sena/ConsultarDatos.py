import mysql.connector 
from conexion_singleton import ConexionSG

def consultarDatos ():
    conexion = ConexionSG.get_conexion("distribuidora_sena")
    cursor = conexion.cursor()
    cursor.execute ("SELECT * FROM clientes")
    return cursor.fetchall()
