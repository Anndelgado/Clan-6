print("Peluquería - Agenda de atención")

corte = 0
cepillado = 0
tintura = 0

total_dia = 0

for i in range(0,7,1):

    nombre = input("\nNombre del cliente: ").strip()

    print("Servicio:")
    print("1. Corte")
    print("2. Cepillado")
    print("3. Tintura")

    servicio = int(input("Elegir: ").strip())
    valor = int(input("Valor pagado: ").strip())

    total_dia += valor

    if servicio == 1:
        corte += 1

    elif servicio == 2:
        cepillado += 1

    elif servicio == 3:
        tintura += 1

    else:
        print("Servicio no válido")

print("\nResumen del día")
print("Total del día:", total_dia)
print("Clientes en corte:", corte)
print("Clientes en cepillado:", cepillado)
print("Clientes en tintura:", tintura)

if corte > cepillado and corte > tintura:
    print("El servicio más solicitado fue: Corte")

elif cepillado > corte and cepillado > tintura:
    print("El servicio más solicitado fue: Cepillado")

else:
    print("El servicio más solicitado fue: Tintura")