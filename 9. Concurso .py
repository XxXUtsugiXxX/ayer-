# 9. Concurso “Adivina el número secreto”
# Como participante, quiero que el programa me pida un número entre 1 y 5 usando un while.
# Si acierto, mostrar “¡Correcto!”.
# Si no, mostrar “Intenta otra vez” y seguir hasta acertar.

import random

numero = random.randint(1, 5)

numero_adivinado = int(input("ingresa un numero de 1 a 5 para ver si adivinaste: "))
while numero_adivinado != numero:
    numero_adivinado = int(input("sigue intentando: "))
    if numero_adivinado != numero:
        numero_adivinado = int(input("sigue intentando: "))
    else:
        print("¡Correcto!")
        break        