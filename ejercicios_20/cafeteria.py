print("Bienvenidos a Café la María")

cafe = 4000
capuchino = 7000
pastel = 6000

total_dia = 0
seguir = True

while seguir:

    producto = input("\n¿Que desea?\n - Cafe\n - Capuchino\n - Pastel\n - Salir:\n ").lower()

    if producto == "salir":
        seguir = False
        break

    cantidad = int(input("Cantidad: "))

    if producto == "cafe":
        total_cliente = cafe * cantidad
        
    elif producto == "capuchino":
        total_cliente = capuchino * cantidad
        
    elif producto == "pastel":
        total_cliente = pastel * cantidad
        
    else:
        print("Producto no válido")
        continue

    if total_cliente > 20000:
        descuento = total_cliente * 0.10
        total_cliente -= descuento
        print("Se aplicó descuento del 10%")

    print("Total a pagar:", total_cliente)

    total_dia += total_cliente

print("\nTotal acumulado del día:", total_dia)