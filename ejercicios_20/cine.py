print("Control de sala de cine")

capacidad = int(input("Ingrese la capacidad total de la sala: ").strip())

total_personas = 0
ninos = 0
adultos = 0
adultos_mayores = 0

for i in range(capacidad):
    edad = int(input("Ingrese la edad de la persona: ").strip())
    
    total_personas += 1

    if edad < 18:
        ninos += 1
    elif edad < 60:
        adultos += 1
    else:
        adultos_mayores += 1

print("\nResumen de la sala")
print("Total de personas:", total_personas)
print("Niños:", ninos)
print("Adultos:", adultos)
print("Adultos mayores:", adultos_mayores)

if total_personas == capacidad:
    print("La sala se llenó")
else:
    print("La sala no se llenó")