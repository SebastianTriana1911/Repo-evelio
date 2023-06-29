import mysql.connector
from conexion_singleton import ConexionSG

def eliminarDatos ():
    conexion = ConexionSG.get_conexion("distribuidora_sena")
    cursor = conexion.cursor ()
    codigo = int(input("Ingrese el codigo que tiene la fila que desea eliminar: "))
    sql = "DELETE FROM clientes WHERE codigo=%s"
    parametro = (codigo,)
    cursor.execute(sql,parametro)
    conexion.commit ()
    return f"\n¡¡ Datos eliminados con exito !!"