# Dada una lista predefinida de nombres, crear un programa que permita al usuario buscar un nombre específico. El algoritmo debe recorrer la lista e indicar si el nombre se encuentra o no en ella, mostrando su posición en caso afirmativo.

nombres = ["Ana", "Luis", "María", "Carlos", "Sofía"]
nombre_buscar = input("Ingrese el nombre que desea buscar: ")
encontrado = False
for i in range(len(nombres)):
    if nombres[i].lower() == nombre_buscar.lower():
        print(f"El nombre '{nombre_buscar}' se encuentra en la posición {i}.")
        encontrado = True
        break
if not encontrado:
    print(f"El nombre '{nombre_buscar}' no se encuentra en la lista.")