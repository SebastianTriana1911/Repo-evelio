from Cuenta import *
class CuentaAhorro(Cuenta):
    def __init__ (self):
        self.__interes = 0

    def getInteres (self):
        return self.__interes
    
    def aplicarInteres (self):
        interes = int(input("Cuanto interes le va agregar a su saldo: "))
        self.__saldo = self.__saldo + interes
        return self.__saldo