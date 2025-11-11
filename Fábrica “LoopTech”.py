# Como supervisor, quiero que un for muestre los productos fabricados del 1 al número que indique el usuario.
# Si el número es par, mostrar “Producto verificado”.
# Si es impar, mostrar “Producto pendiente”.
numero = int(input("digita cuantos productos quieres ver fabricados "))
contador = 1
for i in range(contador, numero+1):
    if contador % 2 == 0:
        print(f"el producto numero {contador} esta verificado")
    else:
        print(f"el producto numero {contador} esta pendiente")
    contador += 1