print("Bienvenido a tu heladeria de confianza")

cono = 3000
vaso = 4000
banana_split = 9000

clientes = 0
total_venta = 0

cant_cono = 0
cant_vaso = 0
cant_banana = 0

seguir = True

while seguir:

    print("Menú:\n Cono\n Vaso\n Banana split")
    product = input("¿Que deseas?: ").strip().lower()
    cantidad = int(input(f"¿Cuantos {product} quieres?: "))

    if product == "cono":
        total = cono * cantidad
        cant_cono += cantidad

    elif product == "vaso":
        total = vaso * cantidad
        cant_vaso += cantidad

    elif product == "banana split":
        total = banana_split * cantidad
        cant_banana += cantidad

    else:
        print("El producto no existe.")
        total = 0

    print("Total a pagar:", total)

    total_venta += total
    clientes += 1

    pregunta = input("Quiere seguir comprando helados si/no: ").strip().lower()

    if pregunta == "no":
        seguir = False


print("\n----- RESUMEN DEL DÍA -----")
print("Clientes atendidos:", clientes)
print("Total vendido:", total_venta)

if cant_cono > cant_vaso and cant_cono > cant_banana:
    print("El producto más pedido fue: Cono")

elif cant_vaso > cant_cono and cant_vaso > cant_banana:
    print("El producto más pedido fue: Vaso")

else:
    print("El producto más pedido fue: Banana split")