# 16. Gasolinera “LoopFuel” – Control de litros vendidos
# Como operador, quiero usar un while que sume litros hasta superar 100.
# Cada vez que se venda una cantidad, verificar:

# Si el total aún es menor que 100 → mostrar “Sigue vendiendo”.
# Si llega o supera 100 → mostrar “Meta diaria alcanzada”
total = 0
litros = int(input("ingresa cuantos litro vendiste: "))
total += litros
while litros < 100:
    litros = int(input("ingresa cuantos mas has vendido: "))
    total += litros
    if total < 100:
        print("sigue vendiendo: ")
    else:
        print("Meta diaria alcanzada: ", total)
        break
else:
    print("Meta diaria alcanzada: ", total)