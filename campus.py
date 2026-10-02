usuario_correcto = "alumno"
clave_correcta = "python123"
acceso = False
for intento in range(1, 4):
    usuario = input(f"Intento {intento}/3 - Usuario: ")
    clave = input("Clave: ")
    if usuario == usuario_correcto and clave == clave_correcta:
        print("Acceso concedido.")
        acceso = True
        break
    else:
        print("Error: credenciales invalidas.")
if acceso == False:
    print("Cuenta bloqueada.")
else:
    while True:
        print()
        print("1) Estado")
        print("2) Cambiar clave")
        print("3) Mensaje")
        print("4) Salir")
        opcion = input("Opcion: ")
        while not opcion.isdigit():
            print("Error: ingrese un numero valido.")
            opcion = input("Opcion: ")
        opcion = int(opcion)
        while opcion < 1 or opcion > 4:
            print("Error: opcion fuera de rango.")
            opcion = input("Opcion: ")
            while not opcion.isdigit():
                print("Error: ingrese un numero valido.")
                opcion = input("Opcion: ")
            opcion = int(opcion)
        if opcion == 1:
            print("Inscripto")
        elif opcion == 2:
            nueva_clave = input("Nueva clave: ")
            if len(nueva_clave) < 6:
                print("Error: minimo 6 caracteres.")
            else:
                confirmacion = input("Confirme la nueva clave: ")
                if nueva_clave == confirmacion:
                    clave_correcta = nueva_clave
                    print("Clave cambiada correctamente.")
                else:
                    print("Error: las claves no coinciden.")
        elif opcion == 3:
            print("Segui adelante, cada paso te acerca a tu objetivo.")
        elif opcion == 4:
            print("Sesion finalizada.")
            break