# Implementar una función llamada factorial que calcule el factorial de un número usando recursión. La función debe recibir un número entero positivo y retornar su factorial. Incluir validación para números negativos.

def factorial(n):
    if n < 0:
        raise ValueError("El número debe ser un entero positivo.")
    elif n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)
    
try:
    print(factorial(5))  
    print(factorial(0))  
    print(factorial(-3))
    
except ValueError as e:
    print(e)
    

