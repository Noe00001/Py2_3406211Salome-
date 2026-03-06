#Ejercicio 1.4 – Validador de contraseña segura: Implementar un sistema que valide la fortaleza de una contraseña. El usuario debe ingresar una contraseña y el algoritmo debe verificar que cumpla con los siguientes criterios: tener al menos 8 caracteres, contener al menos una letra mayúscula, un número y un carácter especial (!@#$%^&*). Informar específicamente qué criterios no se cumplen.

contraseña = input("Ingrese una contraseña: ")  
criterios_no_cumplidos = []
if len(contraseña) < 8:
    criterios_no_cumplidos.append("tener al menos 8 caracteres")
    
if not any(c.isupper() for c in contraseña):
    criterios_no_cumplidos.append("contener al menos una letra mayúscula")
    
if not any(c.isdigit() for c in contraseña):
    criterios_no_cumplidos.append("contener al menos un número")
    
if not any(c in "!@#$%^&*" for c in contraseña):
    criterios_no_cumplidos.append("contener al menos un carácter especial (!@#$%^&*)")
    
if criterios_no_cumplidos:
    print("La contraseña no es segura. Debe cumplir con los siguientes criterios:")
    for criterio in criterios_no_cumplidos:
        print("- " + criterio)
        
else:
    print("La contraseña es segura.")
