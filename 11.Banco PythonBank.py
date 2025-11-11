# 11. Banco “PythonBank” – Simulación de ahorro mensual
# Como cliente, quiero usar un for que sume mi ahorro mensual durante 6 meses.
# Si en algún mes el total supera $1,000,000, mostrar “¡Meta alcanzada!”.
# Al final, mostrar el total acumulado.
ahorrado = 0
for i in range(0, 6):
    ahorro = float(input("cuanto quieres ahorrar este mes"))
    ahorrado += ahorro
    if ahorrado > 1000000:
        print("Meta alcanzada")
        break
print("el total ahorrado es de: ", ahorrado)


    