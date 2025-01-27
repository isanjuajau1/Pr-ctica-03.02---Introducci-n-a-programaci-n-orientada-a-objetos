producto = producto("001", "Laptop", 1200.50)

# Acceder a los atributos y métodos
print(producto)  # Usa el método __str__
print(f"Precio unitario: {producto.precio}€")

# Calcular el precio total para 3 unidades
unidades = 3
precio_total = producto.calcular_total(unidades)
print(f"Precio total para {unidades} unidades: {precio_total}€")