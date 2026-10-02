nombre = input("Ingrese el nombre del cliente: ")
while not nombre.isalpha():
    print("Error: el nombre solo puede contener letras y no puede estar vacio.")
    nombre = input("Ingrese el nombre del cliente: ")
cantidad = input("Ingrese la cantidad de productos: ")
while not cantidad.isdigit() or int(cantidad) <= 0:
    print("Error: ingrese un numero entero mayor que 0.")
    cantidad = input("Ingrese la cantidad de productos: ")
cantidad = int(cantidad)
total_sin_descuentos = 0
total_con_descuentos = 0
for i in range(1, cantidad + 1):
    precio = input(f"Producto {i} - Precio: ")
    while not precio.isdigit():
        print("Error: ingrese un precio entero valido.")
        precio = input(f"Producto {i} - Precio: ")
    precio = int(precio)
    descuento = input("Descuento (S/N): ")
    while descuento.lower() != "s" and descuento.lower() != "n":
        print("Error: ingrese S o N.")
        descuento = input("Descuento (S/N): ")
    total_sin_descuentos += precio
    if descuento.lower() == "s":
        precio_final = precio * 0.90
    else:
        precio_final = precio
    total_con_descuentos += precio_final
ahorro = total_sin_descuentos - total_con_descuentos
promedio = float(total_con_descuentos) / cantidad
print()
print(f"Cliente: {nombre}")
print(f"Total sin descuentos: ${total_sin_descuentos}")
print(f"Total con descuentos: ${total_con_descuentos:.2f}")
print(f"Ahorro: ${ahorro:.2f}")
print(f"Promedio por producto: ${promedio:.2f}")