import mysql.connector
from conexion_singleton import ConexionSG

def insertarDatos ():
    conexion = ConexionSG.get_conexion("distribuidora_sena")
    codigo = int(input("Ingrese codigo: "))
    id = int(input("Ingrese un id: "))
    prim_apellido = (input("Ingrese su pimer apellido: "))
    seg_apellido = input("Ingrese su segundo apellido: ")
    nombre_com = input("Ingrse su nombre completo: ")
    correo = input("Ingrese su correo: ") 
    cursor = conexion.cursor()
    consulta = "INSERT INTO clientes (codigo,id,primer_apellido,segundo_apellido, nombres,correo) VALUES (%s,%s,%s,%s,%s,%s)"
    values = (codigo,id,prim_apellido.upper(),seg_apellido.upper(),nombre_com.upper(),correo)
    cursor.execute (consulta,values)
    conexion.commit()
    return f"\n¡¡ Datos insertados con exito !!"
