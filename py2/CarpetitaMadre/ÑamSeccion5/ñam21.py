# Implementar una función llamada calcular_promedio que reciba una lista de números como parámetro y retorne el promedio de esos números. Incluir validación para listas vacías.

def calcular_promedio(numeros):
    if len(numeros) == 0:
        return "La lista está vacía. No se puede calcular el promedio."
    
    total = sum(numeros)
    promedio = total / len(numeros)
    return promedio

numeros = [10, 20, 30, 40, 50]
print(calcular_promedio(numeros))  
numeros_vacios = []
print(calcular_promedio(numeros_vacios))  