# Desarrollar un sistema que convierta una calificación numérica (0-100) a su equivalente en letras según la siguiente escala: A (90-100), B (80-89), C (70-79), D (60-69), F (0-59). Validar que la nota ingresada esté dentro del rango permitido.

nota = float(input("Ingrese la calificación numérica (0-100): "))
if nota >= 90 and nota <= 100:
    print("La calificación en letras es: A")
elif nota >= 80 and nota < 90:
    print("La calificación en letras es: B")
elif nota >= 70 and nota < 80:
    print("La calificación en letras es: C")
elif nota >= 60 and nota < 70:
    print("La calificación en letras es: D")
elif nota >= 0 and nota < 60:
    print("La calificación en letras es: F")
else:
    print("Calificación no válida. Por favor, ingrese un número entre 0 y 100.")
    
