# 23. Banco “LoopBank” – Simulación de intereses
# Como analista financiero, quiero una función calcularInteres()
# que reciba un monto y una tasa (porcentaje) y retorne el valor final después de aplicar el interés una vez.
# El programa principal debe pedir los datos y mostrar el resultado.
monto = int(input("ingresa monto: "))
tasa = int(input("ingresa la tasa de interes: "))
tasa /= 100
tiempo = int(input("introduce el tiempo: "))
def calcular_interes():
    tasa / 100
    total = monto * tasa * tiempo
    return total

print(calcular_interes())