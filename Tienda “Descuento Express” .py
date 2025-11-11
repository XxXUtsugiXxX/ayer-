# 4. Tienda “Descuento Express” – Clientes atendidos
# Como cajero, quiero usar un for que muestre “Atendiendo cliente número X” del 1 al 8.
# Si el cliente es el número 8, mostrar “Último cliente del día”.
cliente = [1,2,3,4,5,6,7,8]
for cliente in cliente:
    if cliente == 8:
        print("Último cliente del día")
    else:
        print("Atendiendo cliente número: ", cliente)
            