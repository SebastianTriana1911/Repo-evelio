from Cuenta import *
class CuentaCorriente(Cuenta):
    def __init__ (self):
        self.__descuento = int(input("Cuanto va hacer el descuento que va a realizar al salario: "))

    def aplicarDescuento (self):
        resultado = self.__saldo * self.__descuento
        resultadoFinal = resultado // 100
        self.__salario = resultadoFinal
         