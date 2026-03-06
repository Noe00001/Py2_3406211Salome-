# Crear un algoritmo que solicite la edad de una persona y la clasifique en una de las siguientes categorías: niño (0-12 años), adolescente (13-17 años), adulto (18-64 años) o adulto mayor (65 años o más). Mostrar la categoría correspondiente.

edad = int(input("Ingrese su edad: "))
if edad >= 0 and edad <= 12:
    print("Usted es un niño.")
elif edad >= 13 and edad <= 17:
    print("Usted es un adolescente.")
elif edad >= 18 and edad <= 64:
    
    print("Usted es un adulto.")
elif edad >= 65:
    print("Usted es un adulto mayor.")
else:
    print("Edad no válida. Por favor, ingrese una edad positiva.")
    
    
