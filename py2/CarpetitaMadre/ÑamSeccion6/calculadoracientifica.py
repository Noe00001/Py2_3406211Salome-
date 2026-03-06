import math

def calculadora():
    while True:
        print("\n=== CALCULADORA CIENTÍFICA ===")
        print("1. Suma")
        print("2. Resta")
        print("3. Multiplicación")
        print("4. División")
        print("5. Potencia")
        print("6. Raíz cuadrada")
        print("7. Seno")
        print("8. Coseno")
        print("9. Tangente")
        print("10. Logaritmo natural (ln)")
        print("11. Logaritmo base 10")
        print("12. Factorial")
        print("13. Mostrar π y e")
        print("0. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            a = float(input("Ingrese el primer número: "))
            b = float(input("Ingrese el segundo número: "))
            print("Resultado:", a + b)

        elif opcion == "2":
            a = float(input("Ingrese el primer número: "))
            b = float(input("Ingrese el segundo número: "))
            print("Resultado:", a - b)

        elif opcion == "3":
            a = float(input("Ingrese el primer número: "))
            b = float(input("Ingrese el segundo número: "))
            print("Resultado:", a * b)
        elif opcion == "4":
            a = float(input("Ingrese el primer número: "))
            b = float(input("Ingrese el segundo número: "))
            if b != 0:
                print("Resultado:", a / b)
            else:
                print("Error: No se puede dividir por cero.")

        elif opcion == "5":
            a = float(input("Base: "))
            b = float(input("Exponente: "))
            print("Resultado:", math.pow(a, b))

        elif opcion == "6":
            a = float(input("Ingrese el número: "))
            if a >= 0:
                print("Resultado:", math.sqrt(a))
            else:
                print("Error: No se puede calcular raíz de número negativo.")

        elif opcion == "7":
            a = float(input("Ingrese el ángulo en grados: "))
            print("Resultado:", math.sin(math.radians(a)))

        elif opcion == "8":
            a = float(input("Ingrese el ángulo en grados: "))
            print("Resultado:", math.cos(math.radians(a)))

        elif opcion == "9":
            a = float(input("Ingrese el ángulo en grados: "))
            print("Resultado:", math.tan(math.radians(a)))

        elif opcion == "10":
            a = float(input("Ingrese el número: "))
            if a > 0:
                print("Resultado:", math.log(a))
            else:
                print("Error: El logaritmo solo está definido para números positivos.")

        elif opcion == "11":
            a = float(input("Ingrese el número: "))
            if a > 0:
                print("Resultado:", math.log10(a))
            else:
                print("Error: El logaritmo solo está definido para números positivos.")

        elif opcion == "12":
            a = int(input("Ingrese un número entero: "))
            if a >= 0:
                print("Resultado:", math.factorial(a))
            else:
                print("Error: El factorial solo está definido para enteros no negativos.")

        elif opcion == "13":
            print("π =", math.pi)
            print("e =", math.e)

        elif opcion == "0":
            print("Saliendo de la calculadora...")
            break

        else:
            print("Opción no válida.")

calculadora()
