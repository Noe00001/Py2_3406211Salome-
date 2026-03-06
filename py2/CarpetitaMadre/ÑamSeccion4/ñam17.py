# Dada una lista de diccionarios donde cada diccionario representa un producto con las claves "nombre", "precio" y "stock", crear un programa que permita actualizar el precio de un producto específico buscándolo por su nombre.

productos = [
    {"nombre": "Laptop", "precio": 1200.00, "stock": 10},
    {"nombre": "Smartphone", "precio": 800.00, "stock": 20},
    {"nombre": "Tablet", "precio": 500.00, "stock": 15}
]

nombre_producto = input("Ingrese el nombre del producto cuyo precio desea actualizar: ")
encontrado = False
for producto in productos:
    if producto["nombre"].lower() == nombre_producto.lower():
        nuevo_precio = float(input(f"Ingrese el nuevo precio para '{producto['nombre']}': "))
        producto["precio"] = nuevo_precio
        print(f"El precio de '{producto['nombre']}' ha sido actualizado a {nuevo_precio:.2f}.")
        encontrado = True
        break
if not encontrado:
    print(f"El producto '{nombre_producto}' no se encuentra en la lista.")
    