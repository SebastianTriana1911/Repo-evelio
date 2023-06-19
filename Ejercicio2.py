class Persona():
    def __init__ (self,id,codigo,nombre,direccion,telefono):
        self.__id = id
        self.__codigo = codigo
        self.__nombre = nombre
        self.__direccion = direccion
        self.__telefono = telefono
    
    def getId (self):
        return self.__id
    
    def getCodigo (self):
        return self.__codigo
    
    def getNombre (self):
        return self.__nombre
    
    def getDicc (self):
        return self.__direccion
    
    def getTel (self):
        return self.__telefono



class Instructor (Persona):
    def __init__ (self,id,codigo,nombre,direccion,telefono,apellido,numeroID,profesion,especialidad,cargo,salario):
        Persona.__init__(self,id,codigo,nombre,direccion,telefono)
        self.__apellido = apellido
        self.__numeroID = numeroID
        self.__profesion = profesion
        self.__especialidad = especialidad
        self.__cargo = cargo
        self.__salario = salario

    def mostrarInstructor (self):
        print (f"El nombre del instructor es {self.getNombre()} {self.__apellido} y su numero de identidad es {self.__numeroID}")
        print (f"El id que tiene el instructor es {self.getId()} su codigo es {self.getCodigo()}")
        print (f"Su direccion es {self.getDicc()} su telefono de contacto es {self.getTel()}")
        print (f"Su profesion es {self.__profesion} su especialidad es {self.__especialidad} el cargo que maneja es {self.__cargo}")
        print (f"El salario para un instructor en el cargo {self.__cargo} es {self.__salario}")

class Cordinador (Persona):
    def __init__ (self,id,codigo,nombre,direccion,telefono,fecha_ingreso,dir_oficiona,nombre_cordinador):
        Persona.__init__(self,id,codigo,nombre,direccion,telefono)
        self.__fecha_ingreso = fecha_ingreso
        self.__dir_oficina = dir_oficiona
        self.__nombre_cordinacion = nombre_cordinador

    def mostrarCordinador (self):
        print (f"El nombre del cordinador es {self.getNombre()} ")
        print (f"El id que tiene el instructor es {self.getId()} su codigo es {self.getCodigo()}")
        print (f"Su direccion es {self.getDicc()} su telefono de contacto es {self.getTel()}")
        print (f"Su fecha de ingreso fue en {self.__fecha_ingreso} su dir_oficiona es {self.__dir_oficina}")
        print (f"El nombre de codinacion es {self.__nombre_cordinacion}")


instructor1 = Instructor (1,0,"Sebastian","Cra2 #36-50",3214860974,"Triana",1013107003,"Ingeniero","BD","Docente",2000000)
instructor2 = Instructor (2,1,"Andres","Cra2 #36-50",3214860956,"Rodriguez",1013107564,"Ingeniero","BD","Docente",2000000)
instructor3 = Instructor (3,2,"Pedro","Cra2 #36-50",3214860941,"Galarga",10131070789,"Ingeniero","BD","Docente",2000000)
instructor4 = Instructor (4,3,"Camilo","Cra2 #36-50",3214860920,"Zarate",1013107512,"Ingeniero","BD","Docente",2000000)
instructor5 = Instructor (5,4,"Roberto","Cra2 #36-50",3214860949,"Roncancio",1013107512,"Ingeniero","BD","Docente",2000000)

cordinador1 = Cordinador (1,0,"Sebastian","Cra2 #36-50",3214860974,"01-01-2005","Oficiona","Cordinador academico")
cordinador2 = Cordinador (2,1,"Andres","Cra2 #36-50",3214860956,"02-02-2019","Oficina","Cordinador de formacion profecionar")
cordinador3 = Cordinador (3,2,"Pedro","Cra2 #36-50",3214860941,"03-04-2004","Oficina","Cordinador administrativo")
cordinador4 = Cordinador (4,3,"Camilo","Cra2 #36-50",3214860920,"04-05-2022","Oficina","Cordinador articulacion con la media")
cordinador5 = Cordinador (5,4,"Roberto","Cra2 #36-50",3214860949,"08-04-2020","Oficiona","Cordinador programas rurales")

print (instructor1.mostrarInstructor())
print ()
print (instructor2.mostrarInstructor())
print ()
print (instructor3.mostrarInstructor())
print ()
print (instructor4.mostrarInstructor())
print ()
print (instructor5.mostrarInstructor())
print ()
print (cordinador1.mostrarCordinador())
print ()
print (cordinador2.mostrarCordinador())
print ()
print (cordinador3.mostrarCordinador())
print ()
print (cordinador4.mostrarCordinador())
print ()
print (cordinador5.mostrarCordinador())