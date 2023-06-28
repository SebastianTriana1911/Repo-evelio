from Banco import *
from Cliente import *
print ("""Desea crear un banco para saber que opciones puede realizar 
1. Si
2. No
""")
res = (input("Ingrese la opcion que desea realizar: "))
if res == "1":
    banco = Banco()
    print (f"\nBienvenido {banco.getNombreBanco()}\n")
        
    print ("""MENU
1. Actualizar el nombre del banco
2. Agregar cliente a un banco
3. Ver los clientes de un banco
4. Ver un cliente en especifico
5. Obtener el numero de clientes de un banco
6. Salir
""")
    
    salir = True
    while salir:    
        opcion = input("Que opcion desea realizar: ")
        match opcion:
            case "1":
                print (banco.setActualizarNombre())
            case "2":
                cliente = Cliente()
                banco.adicionarCliente(cliente)
                print ("Cliente agregado con exito\n")
            case "3":
                banco.verInfoCLientes()
            case "4":
                banco.buscarCliente()
            case "5":
                print(banco.obtenerNumeroCliente())
            case "6":  
                print ("Adios")
                salir = False
elif res == "2":
    print ("Hasta luego")
else:
    print ("Usted ingreso un dato que no esta en el menu")
