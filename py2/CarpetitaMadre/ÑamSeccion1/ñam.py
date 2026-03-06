# Registro de Usuario: crear un algoritmo que permita registrar los datos de un usuario, el programa debe solicitar el nombre, edad y cuidad de residencia. Luego, mostrar un mensaje personalizado con el siguiente forma: "Hola [Nombre], tienes [edad] años y vivs en [cuidad]." Validar que la edad sea un numero positivo

X = input("Ingrese su nombre: ")
Y = int(input("Ingrese su edad: "))
Z = input("Ingrese su ciudad de residencia: ")

if Y >= 0:
    print(f"Hola {X}, tienes {Y} años y vives en {Z}.")
else:
    print("La edad debe ser un número positivo.")
    