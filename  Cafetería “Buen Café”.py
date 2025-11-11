# 1. Cafetería “Buen Café” – Control de tazas servidas
# Como barista, quiero usar un bucle for para mostrar 
# cuántas tazas he servido del 1 al 10, pero si el número es 5, 
# mostrar el mensaje “¡Mitad del turno completada!”.

contador = 1
for i in range(1, 10):
    if contador == 5:
        print(contador, "vas a mitad de turno completada")
        contador += 1
    elif contador == 10:
        print(contador, "fin del turno")
        break
    print("Taza servida numero: ",contador)
    contador += 1