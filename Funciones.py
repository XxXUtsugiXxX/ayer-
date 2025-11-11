'''def suma (a, b):
    resultado = a + b
    return resultado

total = suma(5,3)
print("la suma es: ", total)'''

# def contar_mayores(lista):
#     contador = 0
#     for numero in lista:
#         if numero >= 5:
#             contador += 1
#     return contador

# numeros = [3, 8, 1, 10, 5, 9]
# resultado = contar_mayores(numeros)
# print("Hay", resultado, "números mayores que 5")

def validarcontraseña():
    contraseñacorrecta = "123"
    contraseñadelusuario = input("ingrese contraseña: ")
    if contraseñacorrecta == contraseñadelusuario:
        print("accediste")
    else:
        print("bloqueada")
validarcontraseña()