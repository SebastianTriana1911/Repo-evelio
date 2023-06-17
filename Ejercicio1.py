lista = []
salida = True
try:
    while salida:
        valor = int(input("Ingrese algo a la lista: "))
        lista.append(valor)
except ValueError:
    lista.append(valor)
    valor = input("Ingrese un valor: ")
    lista.append(valor)
    # if valor == "salir":
    #     lista.pop(-1)
    #     salida = False
print (lista)
print ()
