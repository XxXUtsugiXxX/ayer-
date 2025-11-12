# 20. Aplicación “Inicio Seguro” – Intentos de inicio de sesión
# Como usuario, quiero usar un while con máximo 3 intentos de contraseña.
# Si acierto, mostrar “Acceso permitido”.
# Si agoto los intentos, mostrar “Acceso denegado”.
contador = 1
contraseña = "123"
contraseña_usuario = str(input("digite la contraseña: "))

while contador != 3:
    contador += 1
    if contraseña_usuario != contraseña:
        contraseña_usuario = str(input("acceso denegado: "))
    else:
        print("acceso permitido")
        break
else:
    print("acceso denegado")