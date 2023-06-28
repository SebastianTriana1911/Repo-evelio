import mysql.connector
from mysql.connector import pooling 

# Conexion a la base de datos
class ConexionSG:
    __conexion = None

    @staticmethod
    def get_conexion(bd):
        if ConexionSG.__conexion == None:
            ConexionSG.__conexion = mysql.connector.connect(host = "localhost",
                                                            database = bd,
                                                            user = "root",
                                                            password = "")
        return ConexionSG.__conexion

class MySQLConnectionPool:
    def __init__ (self,pool_name,pool_size,pool_reset_session,host,database,user,password):
        self.__pool_name = pool_name
        self.__pool_size = pool_size
        self.__pool_reset_session = pool_reset_session
        self.__host = host
        self.__database = database
        self.__user = user
        self.__password = password 

mi_pool = pooling.MySQLConnectionPool (pool_name= "pool",
                                       pool_size = 2,
                                       pool_reset_session = True,
                                       host = "localhost",
                                       database = "distribuidora_sena",
                                       user = "root",
                                       password = "")

# Insertar datos en la base de datos
conexion1 = mi_pool.get_connection()
cursor = conexion1.cursor()
cursor.execute("SELECT * FROM clientes")
result = cursor.fetchall()
print(result)
conexion1.close()

