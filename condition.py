'''edad = int(input("introduce tu edad: "))
if edad >= 18:
    print(f"tu edad es {edad} y eres mayor de edad, puedes entrar")
else:
    print(f"tu edad es {edad} y eres menor de edad, no puedes entrar")'''
#Panadería de Don Pancho — Descuentos por cantidades
#'''La panadería de Don Pancho vende pan a $300 cada uno.

#Reglas:

 #   Si compra más de 20 panes → 10% descuento
  #  Si compra más de 50 panes → 20% descuento
   # Si ingresa una cantidad negativa, mostrar "Cantidad inválida"

#Calcular y mostrar el total.'''

'''panes = int(input("Bienvenido, cuantos panes deseas llevar: "))
precio = 300
pago_total = 0
while panes < 0:
    panes = int(input("contidad invalida dijite otra cantidad: "))
if panes >= 1 and panes <=20:
    precio = panes * precio
    print(f"el pago total es: {precio}" )
elif panes > 20 and panes < 50:
    precio = panes * precio
    pago_total = (precio) * (10/100)
    pago_total = precio - pago_total
    print(f"el pago total es: {pago_total}" )
elif panes > 50 :
    precio = panes * precio
    pago_total = (precio) * (20/100)
    pago_total = precio - pago_total
    print(f"el pago total es: {pago_total}" )'''


#'''2. Cine “La Estrella” — Tarifas por edad
'''edad = int(input("introduce tu edad: "))
while edad < 0:
    edad = int(input("edad invalida dijite otra: "))
if edad <= 5 and edad >= 0:
    print(f"tu edad es {edad} puedes entrar gratis")
elif edad > 5 and edad <= 11:
    print(f"tu edad es {edad} y tu boleta vale $5.000")
elif edad >=12 and edad <=59:
     print(f"tu edad es {edad} y tu boleta vale $8.000")
else:
    print(f"tu edad es {edad} y tu boleta vale $4.000 (descuento adulto mayor)")'''

#'''3. Gimnasio “Solo Leveling Fit” — Motivación + Bono'''
#'''Pedir cuántos días entrenó esta semana.

#    ≥ 4 días → "¡Excelente disciplina!" + gana 1 punto de energía
#    2 o 3 → "Bien, pero puedes dar más"
#    0 o 1 → "No aflojes, tú puedes mejorar
#    Mostrar mensaje y si aplica, los puntos ganados.

'''Dias_entrenados = int(input("digita el numero de días entrenados: "))
puntos = 0
while Dias_entrenados < 0:
    Dias_entrenados = int(input("edad invalida dijite otra: "))
if Dias_entrenados >= 4:
        puntos =+ 1
        print(f"¡Excelente disciplina! gana 1 punto de energía, tienes: {puntos} puntos")
elif Dias_entrenados == 2 or Dias_entrenados == 3:
        print(f"Bien, pero puedes dar más, animates mas de momento tienes: {puntos}")
else:
        print(f"No aflojes, tú puedes mejorar {puntos} puntos")'''

#4. Heladería “Frosty” — Sabor y topping
#Sabores y precios:

 #   chocolate → $4.000
  #  vainilla → $3.500

#Opcional: topping cuesta $1.000.

#Si el usuario ingresa un sabor que no existe, mostrar "Sabor no disponible".
#Si el sabor es válido, preguntar si quiere topping y calcular total.

'''print("tenemos estos precios y sabores:")
print("vainilla $3.500")
print("chocolate $4.500")
print("topping $1.000")
sabor_helado = str(input("dijita el sabor de helado que quieres ")).lower()
while sabor_helado != "vainilla" and sabor_helado != "chocolate":
    sabor_helado = str(input("Sabor no disponible, escoge otro: ")).lower()
if sabor_helado == "vainilla":
    topping = int(input("¿quieres un topping? si(1) o no(2) ")).lower()
    if topping == 1:
        print("el valor del helado con el topping es: ", 3.500 + 1.000)
    else:
        print("el valor es ", 3.500)
else: 
    topping = int(input("¿quieres un topping? si o no ")).lower()
    if topping == si:
        print("el valor del helado con el topping es: ", 4.500 + 1.000)
    else:
        print("el valor es ", 4.500)'''

#5. Librería “El Saber” — Descuento estudiante + cupón

#Libro cuesta $25.000.

  #  Si es estudiante → 15% descuento
 #   Si además tiene cupón "LIBRO10" → 10% adicional sobre el valor ya descontado

#Validar:

  #  Si no es estudiante, el cupón no aplica.
 #   Si ingresa cupón incorrecto, ignorarlo.
#
#Mostrar total.

'''estudiante = int(input("si eres estudiante digita 1, si no digita 2: "))
libro = 25000
descuento = libro * 0.15
descuento2 = libro * 0.75
cupon = str()
while estudiante <1 or estudiante >2:
    estudiante = int(input("dijita solo 1 o 2: "))
if estudiante == 1:
    print("el precio de tu libro es de: ", libro - descuento)
    cupon = input("tienes cupon de descuento?, en caso de que si digitalo: ")
    if cupon == "LIBRO10":
        print("el precio de tu libro es de: ", descuento2)
    else:
        print("El precio de tu libro es de: ", descuento)
else:
    print("El precio de tu libro es de: ", libro)'''

#Parqueadero “RapidCar” — Tarifa escalonada
#Tarifa:

  #  0 a 5 horas: $2.000 x hora

 #       5 horas: $2.000 x hora + multa fija de $5.000

#Validar horas:

 #   No permitir números negativos.

#Mostrar valor total.

'''horas = int(input("dijita el numero de horas que estuvo tu vehiculo: "))
while horas < 0:
    horas = int(input("hora invalida dijite otra que sea: ")).lower()
if horas >=0 and horas <= 5:
    print(f"la cantidad de horas es: {horas} y el valor del parqueadero es de: ", horas * 2000)
else:
    print(f"la cantidad de horas es: {horas} yel valor del parqueadero es de: ", horas * 2000 + 5000)'''

#7. Restaurante “El Sabor Colombiano” — Menú + bebida opcional + IVA

#Menú: $12.000

#Opciones bebida:

 #   sí → $3.000
  #  no → $0

#Luego aplicar IVA del 8% al total final.
#Mostrar valor con IVA incluido.

'''menu = 12000
tomar = 3000
menu_tomar = menu + tomar
print("bienvenido al restaurante el sabor de colombia")
print("el menu del día vale: $12000, sin iva incluido")
bebida = str(input("quieres bebida, si o no: ")).lower()
while bebida != "si" and bebida != "no":
    bebida=str(input("digita si o no: ")).lower()
if bebida == "si":
    print("el valor de la bebida es: $3000")
    print("el valor total sin iva incluido es de: ", menu + tomar)
    iva = (menu + tomar) * 0.08 + menu_tomar
    print("el valor total con iva incluido es de: ", iva)
else:
    iva = menu * 0.08 + menu
    print("el valor total con iva incluido es de: ", iva)'''


#8. Empresa “TecnoPlus” — Evaluación compuesta

#El usuario ingresa dos notas (0.0 - 5.0):

  #  Prueba técnica (70%)
 #   Prueba lógica (30%)

#Cálculo: nota_final = (tecnica * 0.7) + (logica * 0.3)

#Condiciones:

   # nota_final ≥ 3 → “Aprobado”
  #  2 ≤ nota_final < 3 → “Revisión”
 #   < 2 → “Reprobado”

#Validar que las notas estén en rango.

'''nota_tecnica = float(input("ingresa la nota sacada en la prueba tecnica solo de 0.0 a 5.0: "))
while nota_tecnica < 0.0 or nota_tecnica > 5.0:
    nota_tecnica = float(input("dijita una nota correcta: "))

nota_logica = float(input("ingresa la nota de la prueba logica solo de 0.0 a 5.0: "))
while nota_logica < 0.0 or nota_logica > 5.0:
    nota_logica = float(input("dijita una nota correcta: "))
calculo_nota_final = (nota_tecnica * 0.7) + (nota_logica * 0.3)

if calculo_nota_final >= 3:
    print ("Aprobado, tu nota es: ", calculo_nota_final)
elif calculo_nota_final >= 2 or calculo_nota_final < 3:
    print("Revisión, tu nota es: ", calculo_nota_final)
else:
    print("Reprobado,  tu nota es: ", calculo_nota_final)'''
 
 #9. Supermercado “AhorroMax” — Descuentos y envío

#Cada producto cuesta $2.000.

#Reglas:

#        30 unidades → 15% descuento
#
 #       10 unidades → 5% descuento
#
#    Si el total después del descuento es < $50.000 → agregar $5.000 de envío

#Calcular total final.
'''print("recuerda que si compras 10 productos tienes 5% de descuento y si son 30 tienes el 15%")
print("por compras inferiores a 50000 se cobran 5000 de envio")
productos = int(input("ingresa la cantidad de productos que compraste: "))
precio = 2000
cantidad = precio * productos
descuento30 = cantidad * 0.85
descuento10 = cantidad * 0.95
if cantidad < 50000:
    descuento10 = descuento10 + 5000
    print("el precio total a pagar es", descuento10)
else:
    print("la cantidad a pagar es de: ", descuento30'''

#10. Club “Noche Estelar” — Acceso + validación documento

#Pedir edad y documento.

#Reglas:

 #   Edad ≥ 18 → puede entrar solo si tiene documento.
  #  Si la edad < 18 → "Entrada denegada"
   # Si tiene 18 o más pero no tiene documento → "Debe presentar documento"

'''documento = str(input("responde si o no, eres mayor de edad ")).lower()

while documento != "si" and documento != "no":
    documento = str(input("responde si o no: "))

if documento == "si":
    documento_muestra = str(input("muestra tienes el documento, si o no: ")).lower()

    while documento_muestra != "si" and documento_muestra != "no":
        documento_muestra = str(input("responde si o no ")).lower()
    if documento_muestra == "si":
        print("puedes entrar")
    else:
        print("debes presentar documento")

else:
    print("entrada denegada")'''

#jercicio: Adivina el número

#Crea un programa en Python que haga lo siguiente:

#El programa genera un número secreto entre 1 y 100 (usa el módulo random para eso).

#El usuario debe intentar adivinar el número.

#Cada vez que el usuario introduce un número:

#Si el número es menor que el secreto, imprime "Demasiado bajo".

#Si el número es mayor que el secreto, imprime "Demasiado alto".

#Si acierta, imprime "¡Correcto!" y termina el programa.

#Usa un bucle while para permitir varios intentos.

#(Opcional) Cuenta cuántos intentos ha hecho el usuario y muestra ese número al final.

'''import random

numero = random.randint(1, 100)
contador = 5

while True:
    try:
        numero_adivinado = int(input("ingresa un numero de 1 a 100 para ver si adivinaste: "))

        for i in range(1, contador):
            while numero_adivinado < 0:
                numero_adivinado = int(input("digita un numero postivo: "))

            while numero_adivinado != numero:
            
                if numero_adivinado < numero:
                    numero_adivinado = int(input(f"estas equivocado el numero es demasiado bajo: {numero_adivinado} ingresa otro numero: "))
                    i =+ 1

                elif numero_adivinado > numero:
                    numero_adivinado = int(input(f"el numero introducido es mas alto, el que elegiste fue {numero_adivinado} ingresa otro numero: "))
                    i =+ 1
                
                break

            else:
                print(f"el numero que pusiste es correcto el numero era: {numero} y el que elegiste fue: {numero_adivinado}")
        
        print("numero de intentos")
            

        break

    except ValueError:
        print ("solo se permite numeros enteros ")'''

#solo se pueden utilizar numero pares del 0 al 100 y si son impares poner numero es impar
#debe tener 7 intentos, no dejar numeros negativos
#si adivina que deje usar un intento mas, y poner lo adivinaste en el anterior

import random
numero = random.randint(0, 100)
contador = 7

while True:
    try:
        if numero % 2 != 0:
            numero =+ 1
        elif numero % 2 == 0:
            numero_adivinado = int(input("ingresa un numero par del 0 al 100: "))
            for i in range (1,contador):

                if numero_adivinado < 0 or numero_adivinado >100 or numero_adivinado % 2 != 0:
                    numero_adivinado = int(input("ingresa un numero valido: "))
                    continue

                if numero_adivinado > numero:
                    numero_adivinado = int(input(f"el numero introducido es mas alto, el que elegiste fue {numero_adivinado} ingresa otro numero: "))
                    i =+ 1
                
                else:
                    numero_adivinado = int(input(f"estas equivocado el numero es demasiado bajo: {numero_adivinado} ingresa otro numero: "))
                    i =+ 1
                    
                if numero_adivinado == numero:
                    numero_adivinado = int(input(f"estas equivocado: "))

                    if numero_adivinado != numero or numero_adivinado == numero:
                        print(f"lo adivinaste en el anterior el numero era {numero}")
                        break
            else:
                print("fallaste")
                break
            
            

    except ValueError:
        print("digita numero positivo")