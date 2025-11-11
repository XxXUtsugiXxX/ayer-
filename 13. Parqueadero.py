# 13. Parqueadero “AutoLoop” – Control de vehículos
# Como vigilante, quiero usar un while que cuente vehículos hasta llegar a 20.
# Si entra un número par, mostrar “Vehículo par registrado”.
# Si el total llega a 20, mostrar “Capacidad completa”.


contador = 1
while contador <= 20:
    contador += 1
    if contador % 2 == 0:
        print(f"Vehiculo numero {contador} registrado")
    if contador == 20:
        print("capacidad completada")
        