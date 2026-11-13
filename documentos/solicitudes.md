## Solicitud INC-014:
* Descripción: El sistema devuelve el precio unitario como subtotal, sin considerar la cantidad solicitada
* Tipo de cambio: Correcion de fallos
* Justificacion: Corregir el error de calculo del subtotal para evitar reclamos de los clientes
* Requisito: RN-01
* Archivos afectados: pedidos.py
* Riesgo: alto
* Criterio de aceptacion: precio unitario x cantidad = subtotal
* Desición: Aprobada
--------------------------
## Solicitud CR-015:
* Descripción: La gerencia solicita incorporar el calculo automatico del costo de encio y el total del pedido
* Tipo de cambio: Agregación de nueva funcionalidad
* Justificacion: Aumentar la eficiencia operativa dentro de la empresa con estos calculos automaticos
* Requisito: RN-02, RN-03, RN-04
* Archivos afectados: pedidos.py
* Riesgo: bajo
* Criterio de aceptacion:
    ** Subtotal >= 300 ---> envio = 0
    ** Subtotal < 300 ----> envio = 20
    ** Total de pedidos = Subtotal + envio
* Desición: Aprobada