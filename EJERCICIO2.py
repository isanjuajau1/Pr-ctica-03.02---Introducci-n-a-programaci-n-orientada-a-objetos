class Producto:
    def __init__(self, codigo, nombre, precio):
        self.codigo = codigo  # Atributo de instancia
        self.nombre = nombre  # Atributo de instancia
        self.precio = precio  # Atributo de instancia

    def __str__(self):
        return f"Producto: {self.nombre} (Código: {self.codigo}, Precio: {self.precio}€)"


class Pedido:
    def __init__(self):
        self.productos = []  # Lista de productos
        self.cantidades = []  # Lista de cantidades

    def agregar_producto(self, producto, cantidad):
        self.productos.append(producto)
        self.cantidades.append(cantidad)

    def total_pedido(self):
        total = 0
        for producto, cantidad in zip(self.productos, self.cantidades):
            total += producto.precio * cantidad
        return total

    def mostrar_productos(self):
        print("Productos en el pedido:")
        for producto, cantidad in zip(self.productos, self.cantidades):
            print(f"{producto.nombre} - Cantidad: {cantidad} - Precio unitario: {producto.precio}€")
            # Crear algunos productos
producto1 = Producto("001", "Laptop", 1200.50)
producto2 = Producto("002", "Smartphone", 800.00)
producto3 = Producto("003", "Tablet", 300.00)

# Crear un pedido
pedido = Pedido()

# Agregar productos al pedido
pedido.agregar_producto(producto1, 2)
pedido.agregar_producto(producto2, 1)
pedido.agregar_producto(producto3, 3)

# Mostrar los productos del pedido
pedido.mostrar_productos()

# Calcular y mostrar el total del pedido
print(f"Total del pedido: {pedido.total_pedido()}€")