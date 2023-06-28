from Cliente import *
class Cuenta:
    def __init__ (self):
        self.__numero = int(input("Cual va a ser su numero de cuenta: "))
        self.__tipo = input ("""Que tipo de cuenta va a tener: 
1. Ahorro
2. Corriente
""")