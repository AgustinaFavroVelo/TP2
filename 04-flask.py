#--------------------------------------------------------------------
# Instalar con pip install Flask
from flask import Flask, request, jsonify
from flask import request
# Instalar con pip install flask-cors
from flask_cors import CORS
# Instalar con pip install mysql-connector-python
import mysql.connector
# Si es necesario, pip install Werkzeug
from werkzeug.utils import secure_filename
# No es necesario instalar, es parte del sistema standard de Python
import os
import time
#--------------------------------------------------------------------

app = Flask(__name__) #determinamos nombre de modulo que estamos ejecutando
CORS(app) #Habilita CORS para todas las rutas

class Catalogo:

    def __init__(self,host, user, password, database): #constructor de clase
        #establecemos primero conexion sin especificar base de datos
        self.conn = mysql.connector.connect(
            host=host,
            user=user,
            password=password
        )
        self.cursor = self.conn.cursor()

        #Intentamos seleccionar la base de datos con try except
        try:
            self.cursor.execute(f"USE {database}")
        except mysql.connector.Error as err:
        # Si la base de datos no existe, la creamos
            if err.errno == mysql.connector.errorcode.ER_BAD_DB_ERROR:
                self.cursor.execute(f"CREATE DATABASE {database}")
                self.conn.database = database
            else:
                raise err
    # Una vez que la base de datos está establecida, creamos la tabla si no existe
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS productos (
            codigo INT,
            descripcion VARCHAR(255) NOT NULL,
            cantidad INT NOT NULL,
            precio DECIMAL(10, 2) NOT NULL,
            imagen_url VARCHAR(255),
            proveedor INT)''')
        self.conn.commit()

    # Config del cursor: Cerrar el cursor inicial y abrir uno nuevo con el parámetro
        dictionary=True
        self.cursor.close()
        self.cursor = self.conn.cursor(dictionary=True) #le digo que trabaje con dic

    def listar_productos(self):
    # Mostramos en pantalla un listado de todos los productos en la tabla
        self.cursor.execute("SELECT * FROM productos")
        productos = self.cursor.fetchall() #traigo todos los datos en forma de dict
        return productos
    
    def consultar_producto(self, codigo):
    # Consultamos un producto a partir de su código
        self.cursor.execute(f"SELECT * FROM productos WHERE codigo = {codigo}")
        return self.cursor.fetchone()

    def mostrar_producto(self, codigo):
        # Mostramos los datos de un producto a partir de su código
        producto = self.consultar_producto(codigo)
        if producto:
            print("-" * 40)
            print(f"Código.....: {producto['codigo']}")
            print(f"Descripción: {producto['descripcion']}")
            print(f"Cantidad...: {producto['cantidad']}")
            print(f"Precio.....: {producto['precio']}")
            print(f"Imagen.....: {producto['imagen_url']}")
            print(f"Proveedor..: {producto['proveedor']}")
            print("-" * 40)
        else:
            print("Producto no encontrado.")

#--------------------------------------------------------------------
# Cuerpo del programa ppal
#--------------------------------------------------------------------
# Crear una instancia de la clase Catalogo
catalogo = Catalogo(host='localhost', user='root', password='', database='miapp')

# Carpeta para guardar las imagenes
ruta_destino = './static/imagenes/'

#Aca van las rutas

@app.route("/productos", methods=["GET"]) #incluyo endpoint 
def listar_productos():           #funcion decorada -> llama productos en forma de dic
    productos = catalogo.listar_productos()
    return jsonify(productos) #jasonifico lo que recibe, lo convierto en json

@app.route("/productos/<int:codigo>", methods=["GET"]) 
def mostrar_producto(codigo):
    producto = catalogo.consultar_producto(codigo)
    if producto:
        return jsonify(producto)
    else:
        return "producto no encontrado", 404
    
if __name__ == "__main__": #inicializamops servidor web de flask como programa ppal en modo debug 
    app.run(debug=True) 


