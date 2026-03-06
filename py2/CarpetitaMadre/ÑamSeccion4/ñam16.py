# Crear un directorio de contactos utilizando diccionarios, donde cada contacto tenga un nombre (clave) y un número telefónico (valor). El sistema debe permitir agregar nuevos contactos, buscar contactos por nombre y eliminar contactos existentes.

contactos = {}
def agregar_contacto():
    nombre = input("Ingrese el nombre del contacto: ")
    numero = input("Ingrese el número telefónico del contacto: ")
    contactos[nombre] = numero
    print(f"Contacto '{nombre}' agregado exitosamente.")
def buscar_contacto():
    nombre = input("Ingrese el nombre del contacto a buscar: ")
    if nombre in contactos:
        print(f"El número telefónico de '{nombre}' es: {contactos[nombre]}")
    else:
        print(f"Contacto '{nombre}' no encontrado.")
def eliminar_contacto():
    nombre = input("Ingrese el nombre del contacto a eliminar: ")
    if nombre in contactos:
        del contactos[nombre]
        print(f"Contacto '{nombre}' eliminado exitosamente.")
    else:
        print(f"Contacto '{nombre}' no encontrado.")
while True:
    print("\nOpciones:")
    print("1. Agregar contacto")
    print("2. Buscar contacto")
    print("3. Eliminar contacto")
    print("4. Salir")
    
    opcion = input("Seleccione una opción (1-4): ")
    
    if opcion == '1':
        agregar_contacto()
    elif opcion == '2':
        buscar_contacto()
    elif opcion == '3':
        eliminar_contacto()
    elif opcion == '4':
        print("Saliendo del programa. ¡Hasta luego!")
        break
    else:
        print("Opción no válida. Por favor, seleccione una opción entre 1 y 4.")