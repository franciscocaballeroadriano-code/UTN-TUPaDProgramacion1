nombre = input("Nombre del Gladiador: ")
while not nombre.isalpha():
    print("Error: Solo se permiten letras.")
    nombre = input("Nombre del Gladiador: ")
vida_jugador = 100
vida_enemigo = 100
pociones = 3
ataque_pesado = 15
daño_enemigo = 12
turno_jugador = True
juego_activo = True
print()
print("=== INICIO DEL COMBATE ===")
while vida_jugador > 0 and vida_enemigo > 0 and juego_activo == True:
    if turno_jugador == True:
        print()
        print(f"{nombre} (HP: {vida_jugador}) vs Enemigo (HP: {vida_enemigo}) | Pociones: {pociones}")
        print("Elige accion:")
        print("1. Ataque Pesado")
        print("2. Rafaga Veloz")
        print("3. Curar")
        opcion = input("Opcion: ")
        while not opcion.isdigit():
            print("Error: Ingrese un numero valido.")
            opcion = input("Opcion: ")
        opcion = int(opcion)
        while opcion < 1 or opcion > 3:
            print("Error: opcion fuera de rango.")
            opcion = input("Opcion: ")
            while not opcion.isdigit():
                print("Error: Ingrese un numero valido.")
                opcion = input("Opcion: ")
            opcion = int(opcion)
        if opcion == 1:
            if vida_enemigo < 20:
                daño = ataque_pesado * 1.5
                vida_enemigo -= daño
                print(f"Golpe Critico! Atacaste al enemigo por {daño} puntos de dano.")
            else:
                daño = float(ataque_pesado)
                vida_enemigo -= daño
                print(f"Atacaste al enemigo por {daño} puntos de dano.")
        elif opcion == 2:
            print("Inicias una rafaga de golpes!")
            for i in range(3):
                vida_enemigo -= 5
                print("> Golpe conectado por 5 de daño")
        elif opcion == 3:
            if pociones > 0:
                vida_jugador += 30
                if vida_jugador > 100:
                    vida_jugador = 100
                pociones -= 1
                print("Usaste una pocion y recuperaste 30 puntos de vida.")
            else:
                print("No quedan pociones!")
        if vida_enemigo > 0:
            turno_jugador = False
    else:
        print()
        print("El enemigo contraataca!")
        vida_jugador -= daño_enemigo
        print(f"El enemigo te ataco por {daño_enemigo} puntos de daño!")
        turno_jugador = True
print()
if vida_jugador > 0:
    print(f"VICTORIA! {nombre} ha ganado la batalla.")
else:
    print("DERROTA. Has caido en combate.")