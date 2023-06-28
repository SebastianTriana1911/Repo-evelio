class Cliente:
    def __init__ (self):
        self.__cedula = int(input("Ingrese su cedula: "))
        self.__nombre = input("Ingrese su nombre: ")
        self.__cuentaAhorros = 0
        self.__cuentaCorriente = 0
        
    def getNombre (self):
        return self.__nombre
    
    def getCedula (self):
        return self.__cedula
    
    def DatosClientes (self):
        return f"El numero de cedula {self.__cedula} pertenece a {self.__nombre}"
    