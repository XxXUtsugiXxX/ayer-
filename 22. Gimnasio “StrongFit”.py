# 22. Gimnasio “StrongFit” – Cálculo de energía
# Como entrenador, quiero una función calcularEnergia() que reciba un número de repeticiones y devuelva un mensaje:

# Si las repeticiones son menores de 5 → “Necesitas más esfuerzo”.
# Si son 5 o más → “¡Buen trabajo!”.

def calculo_de_energia():
    repeticiones = int(input("ingresa numero de repeticiones: "))
    if repeticiones < 5:
        print("Necesitas mas esfuerzo")
    else:
        print("Buen trabajo")
        
calculo_de_energia()