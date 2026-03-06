# Calculadora basica: desarollar una calculadora simple que solicite al usuario dos numeros y una operacion matematica (+, -, *- /). El algoritmo debe realizar la operacion correspondiente y no mostrar el resultado. Incluir validacion para evitar la division por cero, mostrando un mensaje de error en ese caso.

num1 = float(input("Ingrese el primer número: "))
num2 = float(input("Ingrese el segundo número: "))
operacion = input("Ingrese la operación (+, -, *, /): ")

if operacion == "+":
    resultado = num1 + num2
    print("Resultado:", resultado)

elif operacion == "-":
    resultado = num1 - num2
    print("Resultado:", resultado)

elif operacion == "*":
    resultado = num1 * num2
    print("Resultado:", resultado)

elif operacion == "/":
    if num2 != 0:
        resultado = num1 / num2
        print("Resultado:", resultado)
    else:
        print("No quiero: No se puede dividir por cero.")

else:   
    print("Operación no válida.")