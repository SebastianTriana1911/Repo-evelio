import mysql.connector
from conexion_singleton import ConexionSG

conexion = ConexionSG.get_conexion("distribuidora_sena")
cursor = conexion.cursor ()
cursor.execute ("UPDATE clientes SET codigo =%s WHERE id =%s", (51,1013107002))
conexion.commit ()