#conector -> para que bbdd y python interactuen (con mysql connector connect)
#cursor -execute -> para reproducir las operaciones del crud

import mysql.connector

class Catalogo:
    #inicializo
    def __init__(self, host, user, password, database):
        self.conn = mysql.connector.connect ( #parametros de conexion aca
            host= host,
            user= user,
            password = password,
            database = database,
        )

        self.cursor = self.conn.cursor(dictionary=True) #llamo a metodo cursor y pondo dict =true para que me devuelva datos en forma de dic
        self.cursor.execute ('''CREATE TABLE IF NOT EXISTS productos (
                             codigo INT,
                             descripcion VARCHAR(255) NOT NULL,
                             cantidad INT(4) NOT NULL,
                             precio DECIMAL (19,2) NOT NULL,
                             imagen_url VARCHAR (255),
                             proveedor INT(2))''')   
        self.conn.commit()

# ------------------------------- programa ppal. -----------------------------------
catalogo = Catalogo(host='localhost', user='root', password=' ', database='miapp')

