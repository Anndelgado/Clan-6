print("Bienvenidos a Gymbrou")

bajo = 0
medio = 0
alto = 0

for i in range(5):
    nombre = input("Nombre de la persona: ").strip()
    dias = int(input("Días asistidos en la semana: ").strip())
    minutos = int(input("Minutos promedio entrenados por día: ").strip())

    if dias < 3:
        print(nombre, "tiene bajo compromiso")
        bajo += 1
    elif dias <= 4:
        print(nombre, "tiene compromiso medio")
        medio += 1
    else:
        print(nombre, "tiene compromiso alto")
        alto += 1

print("\nResultados finales:")
print("Bajo compromiso:", bajo)
print("Compromiso medio:", medio)
print("Compromiso alto:", alto)