energia = 100
tiempo = 12
cerraduras = 0
alarma = False
codigo = ""
racha = 0
nombre = input("Nombre del agente: ")
while not nombre.isalpha():
    print("Error: solo letras")
    nombre = input("Nombre del agente: ")
while energia > 0 and tiempo > 0 and cerraduras < 3 and not alarma:
    print("\nEnergia:", energia, "| Tiempo:", tiempo)
    print("Cerraduras:", cerraduras)
    print("1. Forzar cerradura")
    print("2. Hackear panel")
    print("3. Descansar")
    opcion = input("Opcion: ")
    while not opcion.isdigit() or int(opcion) < 1 or int(opcion) > 3:
        print("Opcion invalida")
        opcion = input("Opcion: ")
    opcion = int(opcion)
    if opcion == 1:
        racha += 1
        energia -= 20
        tiempo -= 2
        if racha == 3:
            alarma = True
            print("La cerradura se trabo. Alarma activada.")
        elif energia < 40:
            riesgo = input("Elija un numero del 1 al 3: ")
            while not riesgo.isdigit() or int(riesgo) < 1 or int(riesgo) > 3:
                riesgo = input("Elija un numero del 1 al 3: ")
            if int(riesgo) == 3:
                alarma = True
                print("Alarma activada.")
            else:
                cerraduras += 1
                print("Cerradura abierta.")
        else:
            cerraduras += 1
            print("Cerradura abierta.")
    elif opcion == 2:
        racha = 0
        energia -= 10
        tiempo -= 3
        for i in range(4):
            codigo += "A"
            print("Hackeando...", codigo)
        if len(codigo) >= 8 and cerraduras < 3:
            cerraduras += 1
            print("Cerradura abierta.")
    else:
        racha = 0
        energia = min(100, energia + 15)
        tiempo -= 1
        if alarma:
            energia -= 10
        print("Has descansado.")
    if alarma and tiempo <= 3 and cerraduras < 3:
        print("Sistema bloqueado.")
        break
if cerraduras == 3:
    print("\nVICTORIA")
elif alarma:
    print("\nDERROTA: alarma activada.")
else:
    print("\nDERROTA: sin energia o sin tiempo.")