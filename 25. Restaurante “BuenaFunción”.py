# 25. Restaurante “BuenaFunción” – Verificación de turno
# Como gerente, quiero una función verificarTurno(hora) que determine:

# Si la hora es menor que 12 → “Turno de mañana”.
# Si está entre 12 y 18 → “Turno de tarde”.
# Si es mayor → “Turno de noche”.
# El programa principal debe pedir la hora e imprimir el resultado.

hora = int(input("digita el la hora: "))

def verificarTurno(hora):
    if hora < 12:
        print("Turno de mañana")
    elif hora >= 12 and hora < 18:
        print("Turno tarde")
    else:
        print("Turno de noche")
        
verificarTurno(hora)