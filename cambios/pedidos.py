def calcular_subtotal(precio, cantidad):
    subtotal = precio * cantidad 
    return subtotal
precio = 80
cantidad = 3
subtotal = calcular_subtotal(precio,cantidad)
print("subtotal : s/", subtotal)