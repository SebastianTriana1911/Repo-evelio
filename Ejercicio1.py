listaLenguaje = []
listaRegionales = []
listaPares = []
listaMultiplos_4 = []
lista_2693630 = []
listaLetras = []

def llenarList (lista):
    salir = True
    while salir:
        valor = input("Ingrese un valor a la lista: ")
        if valor not in lista:
            lista.append(valor)
        if valor == "salir":
            lista.pop(-1)
            salir = False
    return lista

def posicionList (lista):
    try:
        posicion = int(input("Ingrese la posicion de la que desea saber el elemento: "))
        return print (f"El elemento que se encuentra en la posicion {posicion} es: {lista[posicion]}")
    except:
        return print ("La posicion que ingreso no existe en la lista")

def mayusculas (lista):
    cont = 0
    for i in lista:
        mayuscula = i.upper()
        lista[cont] = mayuscula
        cont = cont + 1
    return lista

def pares (lista):
    try:
        salir = True
        while salir:
            numero = int(input("Ingrese un numero: "))
            if numero % 2 == 0 and numero not in lista:
                lista.append(numero)
            if numero < 0:
                salir = False
        return lista
    except:
        print ("Lo que usted acaba de ingresar no es un numero")

def multiplos (lista):
    try:
        salir = True
        while salir:
            resultado = 0
            numero = int(input("Ingrese un numero: "))
            resultado = 4 * numero 
            lista.append (resultado)
            if numero < 0:
                lista.pop(-1)
                salir = False
        return lista
    except:
        print ("Lo que usted acaba de ingresar no es un numero")

def llenarListMay (lista):
    try:
        salir = True
        while salir:
            nombre = input("Ingrese un nombre a la lista: ")
            if nombre not in lista:
                mayuscula =nombre.upper()
            if mayuscula not in lista:
                lista.append(mayuscula)
            if nombre == "salir":
                lista.pop(-1)
                salir = False
        return lista
    except:
        return print ("lo que ingreso no es un nombre")

def letras (lista):
    salir = True
    while salir:
        letras = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
        valor = input("Ingrese una letra: ")
        if valor in letras:
            lista.append(valor)
            if valor == "salir":
                lista.pop(-1)
        else:
            print ("Lo que ingreso no es una letra")
            salir = False
            return lista


llenarList(listaLenguaje)
print (f"Esta es la lista de lenguajes {listaLenguaje}\n")
print (f"{posicionList(listaLenguaje)}\n")
mayusculas(listaLenguaje)
print (f"Esta es la lista de lenguajes en mayuscula {listaLenguaje}\n")

llenarList(listaRegionales)
print (f"Esta es la lista de regionales del SENA {listaRegionales}\n")
print (f"{posicionList(listaRegionales)}\n")
mayusculas(listaRegionales)
print (f"Esta es la lista de regionales del SENA en mayuscula {listaRegionales}\n")

pares(listaPares)
print (f"La lista de los pares es: {listaPares}")

multiplos(listaMultiplos_4)
print (f"\nLa lista de los multiplos de 4 es: {listaMultiplos_4}")

llenarListMay (lista_2693630)
print (f"\nLa lista de los integrantes de la ficha 2693630 es {lista_2693630}")

letras(listaLetras)
print (f"\nLa lista de las letras es: {listaLetras}")

