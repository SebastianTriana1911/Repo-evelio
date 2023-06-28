from Cliente import *
class Banco:
    def __init__ (self):
        self.__nombre = input("El nombre del banco es: ")
        self.__clientes = []
        
    def setActualizarNombre (self):
        nuevoNombre = input("Como sera el nuevo nombre de su banco: ")
        self.__nombre = nuevoNombre
        return f"Ahora le damos la bienvenida a el banco {self.__nombre}"
    
    def getNombreBanco (self):
        return self.__nombre
    
    def adicionarCliente (self,cliente):
        return self.__clientes.append(cliente)
            
    def obtenerNumeroCliente (self):
        cont = 0
        for i in self.__clientes:
            cont = cont + 1
        return f"\nLa cantidad de clientes con la que cuenta el banco es de {cont} clientes\n"
    
    def verInfoCLientes (self):
        for i in self.__clientes:
            print (f"{i.DatosClientes()}")
            
    def buscarCliente (self):
        cedula = int(input("Ingrese la cedula de la persona a la que quiere buscar: "))
        for i in self.__clientes:
            if cedula == i.getCedula():
                print (f"""Los datos de dicho numero de cedula son:
Nombre: {i.getNombre()}
Cedula: {i.getCedula()}\n""")