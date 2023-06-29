import mysql.connector
from conexion_singleton import ConexionSG
from EliminarDatos import *
from ModificarDatos import *
from MostrarDatos import *
from InsertarDatos import *

print ("""
------------------------|
                        |
MENU                    |
1. Consultar datos      |
2. Insertar datos       |
3. Modificar datos      | 
4. Eliminar datos       |
5. Salir                |
                        |
------------------------|
""")
salir = True
while salir:
    opcion = input("\nIngrese la opcion que desea realizar del menu: ")
    match opcion:
        case "1": 
            print ("Los datos que estan en la tabla clientes son: \n")
            mostrarDatos()
        case "2":
            print ("Insertemos datos a la tabla clientes")
            print(insertarDatos())
        case "3":
            print ("\nModifiquemosle algun dato a la tabla clientes")
            print (modificarDatos())
        case "4":
            print ("\nEliminemos datos de la tabla clientes")
            print (eliminarDatos())
        case "5":
            break



