# Implementar un programa que permita al usuario ingresar dos listas de elementos. El algoritmo debe mostrar: los elementos comunes a ambas listas, los elementos únicos de la primera lista y los elementos únicos de la segunda lista, implementando esta lógica con ciclos sin usar funciones de conjuntos.

lista1_input = input("Ingrese la primera lista de elementos separados por comas: ")
lista2_input = input("Ingrese la segunda lista de elementos separados por comas: ")
lista1 = [elemento.strip() for elemento in lista1_input.split(",")]
lista2 = [elemento.strip() for elemento in lista2_input.split(",")]

elementos_comunes = []

for elemento in lista1:
    if elemento in lista2 and elemento not in elementos_comunes:
        elementos_comunes.append(elemento)
        
elementos_unicos_lista1 = []

for elemento in lista1:
    if elemento not in lista2 and elemento not in elementos_unicos_lista1:
        elementos_unicos_lista1.append(elemento)
        
elementos_unicos_lista2 = []

for elemento in lista2:
    
    if elemento not in lista1 and elemento not in elementos_unicos_lista2:
        elementos_unicos_lista2.append(elemento)

print("Elementos comunes a ambas listas:")
print(elementos_comunes)
print("Elementos únicos de la primera lista:")
print(elementos_unicos_lista1)
print("Elementos únicos de la segunda lista:")
print(elementos_unicos_lista2)

