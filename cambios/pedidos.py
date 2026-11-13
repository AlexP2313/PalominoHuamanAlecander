def calcular_subtotal(precio, cantidad):
    subtotal = precio * cantidad 
    return subtotal
def costo_de_envio(subtotal):
    if subtotal >= 300:
        return 0
    else:
        return 20
def calcular_total(subtotal, costo_envio):
    total = subtotal + costo_envio
    return total
precio = 150
cantidad = 3
subtotal = calcular_subtotal(precio,cantidad)
costo_envio = costo_de_envio(subtotal)
total = calcular_total(subtotal, costo_envio)
print("subtotal : s/", subtotal)
print("costo de envio : s/", costo_envio)
print("total : s/", total)
