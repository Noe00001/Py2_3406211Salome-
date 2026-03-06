#Ejercicio 1.5 – Convertidor de unidades con menú: Desarrollar un convertidor de unidades con un menú interactivo que ofrezca tres opciones: 1. Convertir Celsius a Fahrenheit, 2. Convertir kilómetros a millas, 3. Convertir kilogramos a libras. El usuario debe seleccionar una opción, ingresar el valor a convertir y el programa mostrará el resultado con dos decimales.

print("Seleccione una opción:")
print("1. Convertir Celsius a Fahrenheit")
print("2. Convertir kilómetros a millas")
print("3. Convertir kilogramos a libras")

opcion = input("Ingrese el número de la opción deseada: ")
if opcion == "1":
    celsius = float(input("Ingrese la temperatura en Celsius: "))
    fahrenheit = (celsius * 9/5) + 32
    print(f"{celsius:.2f} °C son {fahrenheit:.2f} °F")
    
elif opcion == "2":
    kilometros = float(input("Ingrese la distancia en kilómetros: "))
    millas = kilometros * 0.621371
    print(f"{kilometros:.2f} km son {millas:.2f} millas")
    
elif opcion == "3":
    kilogramos = float(input("Ingrese el peso en kilogramos: "))
    libras = kilogramos * 2.20462
    print(f"{kilogramos:.2f} kg son {libras:.2f} libras")
    
else:
    print("Opción no válida. Por favor, seleccione una opción del 1 al 3.")