from Cliente import *
class Cuenta:
    def __init__ (self):
        self.__numero = int(input("Cual va a ser su numero de cuenta: "))
        self.__saldo = 0

    def getNumero (self):
        return self.__numero
    
    def getSaldo (self):
        return self.__saldo