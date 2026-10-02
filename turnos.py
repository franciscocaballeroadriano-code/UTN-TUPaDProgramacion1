operador = input("Nombre del operador: ")
while not operador.isalpha():
    print("Error: solo letras")
    operador = input("Nombre del operador: ")
lunes1 = ""
lunes2 = ""
lunes3 = ""
lunes4 = ""
martes1 = ""
martes2 = ""
martes3 = ""
while True:
    print("\n1. Reservar")
    print("2. Cancelar")
    print("3. Ver agenda")
    print("4. Ver resumen")
    print("5. Salir")
    opcion = input("Opcion: ")
    while not opcion.isdigit() or int(opcion) < 1 or int(opcion) > 5:
        print("Error: opcion invalida")
        opcion = input("Opcion: ")
    opcion = int(opcion)
    if opcion == 1:
        dia = input("Dia (1=Lunes, 2=Martes): ")
        while not dia.isdigit() or int(dia) < 1 or int(dia) > 2:
            print("Error: dia invalido")
            dia = input("Dia (1=Lunes, 2=Martes): ")
        dia = int(dia)
        nombre = input("Nombre del paciente: ")
        while not nombre.isalpha():
            print("Error: solo letras")
            nombre = input("Nombre del paciente: ")
        if dia == 1:
            if nombre in (lunes1, lunes2, lunes3, lunes4):
                print("El paciente ya tiene turno.")
            elif lunes1 == "":
                lunes1 = nombre
            elif lunes2 == "":
                lunes2 = nombre
            elif lunes3 == "":
                lunes3 = nombre
            elif lunes4 == "":
                lunes4 = nombre
            else:
                print("No hay turnos disponibles.")
        else:
            if nombre in (martes1, martes2, martes3):
                print("El paciente ya tiene turno.")
            elif martes1 == "":
                martes1 = nombre
            elif martes2 == "":
                martes2 = nombre
            elif martes3 == "":
                martes3 = nombre
            else:
                print("No hay turnos disponibles.")
    elif opcion == 2:
        dia = input("Dia (1=Lunes, 2=Martes): ")
        while not dia.isdigit() or int(dia) < 1 or int(dia) > 2:
            print("Error: dia invalido")
            dia = input("Dia (1=Lunes, 2=Martes): ")
        dia = int(dia)
        nombre = input("Nombre del paciente: ")
        if dia == 1:
            if nombre == lunes1:
                lunes1 = ""
            elif nombre == lunes2:
                lunes2 = ""
            elif nombre == lunes3:
                lunes3 = ""
            elif nombre == lunes4:
                lunes4 = ""
            else:
                print("Paciente no encontrado.")
        else:
            if nombre == martes1:
                martes1 = ""
            elif nombre == martes2:
                martes2 = ""
            elif nombre == martes3:
                martes3 = ""
            else:
                print("Paciente no encontrado.")
    elif opcion == 3:
        dia = input("Dia (1=Lunes, 2=Martes): ")
        if dia == "1":
            print("Turno 1:", lunes1 if lunes1 else "(libre)")
            print("Turno 2:", lunes2 if lunes2 else "(libre)")
            print("Turno 3:", lunes3 if lunes3 else "(libre)")
            print("Turno 4:", lunes4 if lunes4 else "(libre)")
        else:
            print("Turno 1:", martes1 if martes1 else "(libre)")
            print("Turno 2:", martes2 if martes2 else "(libre)")
            print("Turno 3:", martes3 if martes3 else "(libre)")
    elif opcion == 4:
        ocupados_lunes = (lunes1 != "") + (lunes2 != "") + (lunes3 != "") + (lunes4 != "")
        ocupados_martes = (martes1 != "") + (martes2 != "") + (martes3 != "")
        print("Lunes:", ocupados_lunes, "ocupados,", 4 - ocupados_lunes, "disponibles")
        print("Martes:", ocupados_martes, "ocupados,", 3 - ocupados_martes, "disponibles")
        if ocupados_lunes > ocupados_martes:
            print("El dia con mas turnos es Lunes.")
        elif ocupados_martes > ocupados_lunes:
            print("El dia con mas turnos es Martes.")
        else:
            print("Hay empate.")
    else:
        print("Sistema cerrado.")
        break