# Tomar el menú de calculadora desarrollado en ejercicios anteriores y refactorizarlo, convirtiendo cada operación matemática en una función separada. El menú principal debe llamar a estas funciones según la opción seleccionada.

def sumar(a, b):
    return a + b

def restar(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b == 0:
        raise ValueError("No se puede dividir entre cero.")
    return a / b

def menu_calculadora():
    print("Bienvenido a la calculadora")
    print("Seleccione una operación:")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    
    opcion = input("Ingrese el número de la operación que desea realizar: ")
    
    if opcion in ['1', '2', '3', '4']:
        a = float(input("Ingrese el primer número: "))
        b = float(input("Ingrese el segundo número: "))
        
        try:
            if opcion == '1':
                resultado = sumar(a, b)
                print(f"El resultado de {a} + {b} es: {resultado}")
            elif opcion == '2':
                resultado = restar(a, b)
                print(f"El resultado de {a} - {b} es: {resultado}")
            elif opcion == '3':
                resultado = multiplicar(a, b)
                print(f"El resultado de {a} * {b} es: {resultado}")
            elif opcion == '4':
                resultado = dividir(a, b)
                print(f"El resultado de {a} / {b} es: {resultado}")
        except ValueError as e:
            print(e)
    else:
        print("Opción no válida. Por favor, seleccione una opción del 1 al 4.")