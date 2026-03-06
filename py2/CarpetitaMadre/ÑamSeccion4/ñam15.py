# Implementar un sistema de lista de compras que permita al usuario agregar productos, eliminar productos específicos y mostrar todos los productos actuales. Utilizar una lista para almacenar los elementos.

lista_compras = []
while True:
    print("\nOpciones:")
    print("1. Agregar producto")
    print("2. Eliminar producto")
    print("3. Mostrar lista de compras")
    print("4. Salir")
    
    opcion = input("Seleccione una opción (1-4): ")
    
    if opcion == '1':
        producto = input("Ingrese el nombre del producto a agregar: ")
        lista_compras.append(producto)
        print(f"'{producto}' ha sido agregado a la lista de compras.")
        
    elif opcion == '2':
        producto = input("Ingrese el nombre del producto a eliminar: ")
        if producto in lista_compras:
            lista_compras.remove(producto)
            print(f"'{producto}' ha sido eliminado de la lista de compras.")
        else:
            print(f"'{producto}' no se encuentra en la lista de compras.")
            
    elif opcion == '3':
        if lista_compras:
            print("Lista de compras actual:")
            for idx, item in enumerate(lista_compras, start=1):
                print(f"{idx}. {item}")
        else:
            print("La lista de compras está vacía.")
            
    elif opcion == '4':
        print("Saliendo del programa. ¡Hasta luego!")
        break
        
    else:
        print("Opción no válida. Por favor, seleccione una opción entre 1 y 4.")