print("Control de vehículos")

moto = 0
carro = 0
hcarro = 4000
hmoto = 2000

total = 0

mayor_pago = 0
placa_mayor = ""

for i in range(0, 8, 1):

    placa = input("Ingrese la placa: ")

    print("Tipo de vehículo:\n 1. Carro\n 2. Moto")
    tipo = int(input("Elegir: ").strip())

    horas = int(input("¿Cuántas horas estuvo parqueado? ").strip())

    if tipo == 1:
        pago = hcarro * horas
        carro += 1

    elif tipo == 2:
        pago = hmoto * horas
        moto += 1

    else:
        print("Opción no válida")
        pago = 0

    total += pago

    if pago > mayor_pago:
        mayor_pago = pago
        placa_mayor = placa

print("\nResumen del parqueadero")
print("Total recaudado:", total)
print("Carros ingresados:", carro)
print("Motos ingresadas:", moto)
print("Vehículo que pagó más:", placa_mayor, ", pagó:", mayor_pago)
        

    
