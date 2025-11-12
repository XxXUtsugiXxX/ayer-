# 15. Academia “CodeStart” – Contador de ejercicios completados
# Como estudiante, quiero usar un for del 1 al número que indique.
# Si el número es múltiplo de 5, mostrar “¡Gran avance!”.
# Si no, solo mostrar “Ejercicio X completado”.

contador = int(input("ingrese el numeros de ejercicios terminados: "))
tareas = 1
for i in range(0, contador):
    
    if tareas % 5 != 0:
        print(f"ejercicio {tareas} completado")
        tareas += 1
    else:
        tareas += 1
        print ("¡Gran avance!")