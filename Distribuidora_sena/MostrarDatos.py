import mysql.connector 
from conexion_singleton import ConexionSG

def mostrarDatos ():
    conexion = ConexionSG.get_conexion ("distribuidora_sena")
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM clientes")
    for registro in cursor.fetchall():
        print (f"Codigo = {registro[0]}")
        print (f"Id = {registro[1]}")
        print (f"primer_apellido = {registro[2]}")
        print (f"segundo_apellido = {registro[3]}")
        print (f"nombres = {registro[4]}")
        print (f"correo = {registro[5]}")
        print ("------------------------------------")

# Buscar datos por nombre del campo (atributo)

# conexion = ConexionSG.get_conexion ("distribuidora_sena")
# cursor = conexion.cursor(dictionary = True)
# cursor.execute("SELECT * FROM clientes")
# for registro in cursor.fetchall():
#     print (f"Codigo = {registro['codigo']}")
#     print (f"Id = {registro['id']}")
#     print (f"primer_apellido = {registro['primer_apellido']}")
#     print (f"segundo_apellido = {registro['segundo_apellido']}")
#     print (f"nombres = {registro['nombres']}")
#     print (f"correo = {registro['correo']}")