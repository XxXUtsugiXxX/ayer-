# 2. Cine “La Estrella” – Cuenta regresiva antes de iniciar la función
# Como proyeccionista, quiero mostrar una cuenta regresiva del 5 al 1 usando for.
# Si llega al número 1, debe imprimir “¡Que empiece la función!”.
contador = 5
for i in range(0, 6):
    if contador >= 1:
        print(contador)
        contador -= 1 
    else:
        print("¡Que empiece la función!")  