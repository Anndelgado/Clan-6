print("Tienda de mascotas - Ventas")

alimento = 0
juguete = 0
accesorio = 0

for i in range(0,10,1):

    print("\nCategoría:")
    print("1. Alimento")
    print("2. Juguete")
    print("3. Accesorio")

    categoria = int(input("Elegir: ").strip())
    valor = int(input("Valor de la compra: ").strip())

    if categoria == 1:
        alimento += valor

    elif categoria == 2:
        juguete += valor

    elif categoria == 3:
        accesorio += valor

    else:
        print("Categoría no válida")

print("\nResumen de ventas")
print("Total vendido en alimento:", alimento)
print("Total vendido en juguete:", juguete)
print("Total vendido en accesorio:", accesorio)

if alimento > juguete and alimento > accesorio:
    print("La categoría que generó más dinero fue: Alimento")

elif juguete > alimento and juguete > accesorio:
    print("La categoría que generó más dinero fue: Juguete")

else:
    print("La categoría que generó más dinero fue: Accesorio")