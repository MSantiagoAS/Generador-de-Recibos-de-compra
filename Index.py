#este codigo sera un ejemplo de recibo de compra en python
import datetime

fecha = datetime.datetime.now()
comprador = str(input("Ingrese el nombre del comprador: "))
id_comprador = int(input("Ingrese el ID del comprador: "))
producto = str(input("Ingrese el nombre del producto: "))
cantidad = int(input("Ingrese la cantidad del producto: "))
precio = float(input("Ingrese el precio unitario del producto: "))
fecha_compra = fecha.strftime("%d/%m/%Y %H:%M:%S")
total = cantidad * precio

print("\n----- RECIBO DE COMPRA -----")
print("Fecha y hora:", fecha_compra)
print("Comprador:", comprador)
print("ID del comprador:", id_comprador)
print("Producto:", producto)
print("Cantidad:", cantidad)
print("Precio unitario:", precio)
print("Total a pagar:", total)
