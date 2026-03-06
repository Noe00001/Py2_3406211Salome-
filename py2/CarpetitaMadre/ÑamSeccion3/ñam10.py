# Crear un programa que solicite al usuario un número entero positivo N y muestre todos los números pares desde 1 hasta N utilizando un ciclo for.

N = int(input("Ingrese un número entero positivo: "))
if N > 0:
    print(f"Números pares desde 1 hasta {N}:")
    for i in range(1, N + 1):
        if i % 2 == 0:
            print(i)
else:
    print("Por favor, ingrese un número entero positivo.")
    