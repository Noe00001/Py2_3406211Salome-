# Expandir la calculadora básica del ejercicio 1.2 agregando un menú que permita al usuario realizar múltiples operaciones sin salir del programa. El menú debe incluir las cuatro operaciones básicas y una opción para salir.

def sumar(a, b):
    return a + b

def restar(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b == 0:
        return "Error: No se puede dividir entre cero."
    return a / b

while True:
    print("Seleccione una operación:")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    print("5. Salir")

    opcion = input("Ingrese el número de la opción deseada: ")
    
    if opcion in ["1", "2", "3", "4"]:
        num1 = float(input("Ingrese el primer número: "))
        num2 = float(input("Ingrese el segundo número: "))
        
        if opcion == "1":
            resultado = sumar(num1, num2)
            print(f"El resultado de {num1} + {num2} es: {resultado}")
            
        elif opcion == "2":
            resultado = restar(num1, num2)
            print(f"El resultado de {num1} - {num2} es: {resultado}")
            
        elif opcion == "3":
            resultado = multiplicar(num1, num2)
            print(f"El resultado de {num1} * {num2} es: {resultado}")
            
        elif opcion == "4":
            resultado = dividir(num1, num2)
            print(f"El resultado de {num1} / {num2} es: {resultado}")
            
    elif opcion == "5":
        print("Saliendo del programa. ¡Hasta luego!")
        break
        
    else:
        print("Opción no válida. Por favor, seleccione una opción del 1 al 5.")