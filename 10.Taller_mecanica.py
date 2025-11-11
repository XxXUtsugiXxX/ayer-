# 10. Taller “Mecánica Pro” – Revisiones del día
# Como mecánico, quiero usar un for que muestre “Revisión X”.
# Si X es igual a 3, mostrar “Revisión especial de motor”.
contador = 0
for i in range(0, 4):
    if contador < 3:
        contador += 1    
        print(contador)

    else:
        print(f"revision {contador}, revision especial de motor")