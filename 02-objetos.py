class Catalogo:
    productos= []
    def agregar_producto(self, codigo, descripcion, cantidad, precio, imagen,proveeedor):

        if self.consultar_producto(codigo):
            return False #si esta retorna false y sale
    
        nuevo_producto = {
            'codigo': codigo,
            'descripcion': descripcion,
            'cantidad': cantidad,
            'precio': precio,
            'imagen': imagen,
            'proveeedor': proveeedor,
        }
        self.productos.append(nuevo_producto)
        return True
    
    def consultar_producto (self, codigo):
        for producto in self.productos:
            if producto['codigo'] == codigo: #si es igual, existe
                return producto #retorna el dic entero
        return False

    def listar_productos(self):
        print("-" *50)
        for producto in self.productos:
            print(f"Codigo: {producto['codigo']}")
            print(f"Descripcion: {producto['descripcion']}")
            print(f"Cantidad:  {producto['cantidad']}")
            print(f"Precio: {producto['precio']}")
            print(f"imagen:  {producto['imagen']}")
            print(f"proveeedor:  {producto['proveeedor']}")
            print("-" *50)

    def modificar_producto (self, codigo, nueva_descripcion, nueva_cantidad, nuevo_precio, nueva_imagen,nuevo_proveedor):
        for producto in self.productos:
            if producto['codigo'] == codigo:
                producto['descripcion'] = nueva_descripcion
                producto['cantidad'] = nueva_cantidad
                producto['precio'] = nuevo_precio
                producto['imagen'] = nueva_imagen
                producto['proveeedor'] = nuevo_proveedor
                return True
        return False 

    def eliminar_producto(self, codigo):
        for producto in self.productos:
            if producto['codigo'] == codigo:
                self.productos.remove(producto)
                return True
        return False
    
#------------------------------------programa ppal-----------------------------------
#agregamos productos 
catalogo= Catalogo()
catalogo.agregar_producto(1,'Mouse USB 3 botones',5,2500,'mouse.jpg', 102)
catalogo.agregar_producto(2, 'Laptop 64 GB', 27, 4575566, 'compu.png', 107)
catalogo.listar_productos()


# #modificamos productos
catalogo.modificar_producto(1, 'teclado mecanico 62 teclas', 20 ,23699, 'tecmec.jpg', 106)
catalogo.listar_productos()


# #eliminamos producto
catalogo.eliminar_producto(2)
catalogo.listar_productos()






