import mysql.connector
from conexion_singleton import ConexionSG

conexion = ConexionSG.get_conexion("distribuidora_sena")
cursor = conexion.cursor ()
sql = "DELETE FROM clientes WHERE codigo =%s"
parametro = (50,)
cursor.execute(sql,parametro)
conexion.commit ()