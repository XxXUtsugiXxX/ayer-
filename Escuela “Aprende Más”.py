# 5. Escuela “Aprende Más” – Registro de tareas entregadas
# Como profesor, quiero usar un while que sume tareas hasta 10. Si el contador llega a 10,
# mostrar “¡Todas las tareas recibidas!”. Si aún no llega, mostrar cuántas faltan.
contador = 10
tareas = 1

while tareas < contador:
        print(f"faltan {contador - tareas} resividas: {tareas}")
        tareas += 1
else:
    print("¡Todas las tareas recibidas!")