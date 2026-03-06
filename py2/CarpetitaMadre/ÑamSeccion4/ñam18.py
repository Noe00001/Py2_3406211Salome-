# Desarrollar un programa que solicite al usuario ingresar una lista de números separados por comas. El algoritmo debe calcular y mostrar: el valor máximo, el valor mínimo, el promedio y la suma total de todos los números.

numeros_input = input("Ingrese una lista de números separados por comas: ")
numeros_str = numeros_input.split(",")
numeros = []
for num_str in numeros_str:
    try:
        numero = float(num_str.strip())
        numeros.append(numero)
    except ValueError:
        print(f"'{num_str}' no es un número válido y será ignorado.")
if numeros:
    valor_maximo = max(numeros)
    valor_minimo = min(numeros)
    promedio = sum(numeros) / len(numeros)
    suma_total = sum(numeros)
    print(f"Valor máximo: {valor_maximo}")
    print(f"Valor mínimo: {valor_minimo}")
    print(f"Promedio: {promedio:.2f}")
    print(f"Suma total: {suma_total:.2f}")
else:
    print("No se ingresaron números válidos.")
