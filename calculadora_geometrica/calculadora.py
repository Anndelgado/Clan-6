
print("Bienvenido a la tu calculadora geométrica\n")


print("¿Que quieres hacer?:\n 1. Calcular figuras 2D.\n 2. Calcular figuras 3D.\n 3. Salir.\n").strip()

opcion = int(input("Selecione una opción: "))

#Figura 2D
if opcion == 1:
    print("Figuras 2D:\n 1. Rectángulo.\n 2. Triángulo.\n 3. Círculo.\n 4. Rombo.\n").strip()

    figura2d = int(input("Seleccione una figura: "))

    if figura2d == 1:
        base = float(input("Ingrese la base: "))
        altura = float(input("Ingrese la altura: "))
        area = base * altura
        perimetro = 2 * (base + altura)
        print("Área:", area)
        print("Perímetro:", perimetro)

    elif figura2d == 2:
        base = float(input("Ingrese la base: "))
        altura = float(input("Ingrese la altura: "))
        lado1 = float(input("Ingrese el lado 1: "))
        lado2 = float(input("Ingrese el lado 2: "))
        lado3 = float(input("Ingrese el lado 3: "))
        area = (base * altura) / 2
        perimetro = lado1 + lado2 + lado3
        print("Área:", area)
        print("Perímetro:", perimetro)

