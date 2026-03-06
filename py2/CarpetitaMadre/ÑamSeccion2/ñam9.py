# Crear un simulador de descuentos que solicite al usuario su categoría (A, B, C) y el monto de compra. Aplicar los siguientes descuentos según categoría: A=20%, B=15%, C=10%. Para cualquier otra categoría no aplicar descuento. Mostrar el monto final a pagar y la cantidad ahorrada.

categoria = input("Ingrese su categoría (A, B, C): ").upper()
monto_compra = float(input("Ingrese el monto de compra: "))
if categoria == "A":
    descuento = monto_compra * 0.20
elif categoria == "B":
    descuento = monto_compra * 0.15
elif categoria == "C":
    descuento = monto_compra * 0.10
else:
    descuento = 0
monto_final = monto_compra - descuento
print(f"El monto final a pagar es: ${monto_final:.2f}")
print(f"La cantidad ahorrada es: ${descuento:.2f}")
