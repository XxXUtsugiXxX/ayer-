# 14. Tienda “Ahorra Más” – Caja registradora básica
# Como cajero, quiero pedir montos de venta hasta que el usuario escriba 0.
# Si la venta supera $100,000, mostrar “Venta destacada”.
# Al final, mostrar el total vendido.

total = 0
monto = 1
while monto != 0:
    monto = int(input("ingresa el monto a pagar: "))
    total += monto
    if monto >= 100000:
        print("venta destacada: ", monto)
else:
    print ("este es el total a pagar: ", total)