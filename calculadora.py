from funciones import pedir_float, pedir_opcion

print("Bienvenido a la tu calculadora geométrica\n")

opcion = 0
pi = 3.1416

#Figura 2D
while opcion != 3:  
    print("¿Que quieres hacer?:\n 1. Calcular figuras 2D.\n 2. Calcular figuras 3D.\n 3. Salir.\n")
    opcion = pedir_opcion("Escoge una opción: ", 1, 3)
    if opcion == 3:
        continue
    if opcion == 1:
        print("Figuras 2D:\n 1. Rectángulo.\n 2. Triángulo.\n 3. Círculo.\n 4. Rombo.\n 5. Triángulo rectángulo. \n6. Volver al menu")
        
        figura2d = pedir_opcion("Seleccione una figura: ", 1, 6)
        
        if figura2d == 6:
            continue
        if figura2d == 1:
            print("Elegiste Rectángulo, ¿Que operación deseas hacer?:\n 1. Área.\n 2. Perímetro.\n 3. Volver.")
            
            rectan = pedir_opcion("Elija una: ", 1, 3)
            if rectan == 3:
                continue
            
            elif rectan == 1:
                base = pedir_float("Ingrese la base: ")
                altura = pedir_float("Ingrese la altura: ")
                
                area = base * altura
                print("Área:", area)
            
            elif rectan == 2:
                base = pedir_float("Ingrese la base: ")
                altura = pedir_float("Ingrese la altura: ")
                
                perimetro = 2 * (base + altura)
                print("Perímetro:", perimetro)

        elif figura2d == 2:
            print("Elegiste Triángulo, ¿Que operación deseas hacer?:\n 1. Área.\n 2. Perímetro.\n 3. Ángulo.\n 4. Volver.")
            
            triangulo = pedir_opcion("Elija una: ", 1, 4)
            if triangulo == 4:
                continue
            elif triangulo == 1:
                base = pedir_float("Ingrese la base: ")
                altura = pedir_float("Ingrese la altura: ")
                
                area = (base * altura) / 2
                print("Área:", area)
            
            elif triangulo == 2:
                lado1 = pedir_float("Ingrese el lado 1: ")
                lado2 = pedir_float("Ingrese el lado 2: ")
                lado3 = pedir_float("Ingrese el lado 3: ")
                
                perimetro = lado1 + lado2 + lado3
                print("Perímetro:", perimetro)
            
            elif triangulo == 3:
                an1 = pedir_float("Ingresa ángulo 1: ")
                an2 = pedir_float("Ingresa ángulo 2: ")
                
                if an1 + an2 >= 180:
                   print("Ángulos inválidos.")
                else:
                   an3 = 180 - (an1 + an2)
                   print("El ángulo faltante mide:", an3)
         
        
        elif figura2d == 3:
            print("Elegiste Círculo, ¿Que operación deseas hacer?:\n 1. Área.\n 2. Perímetro.\n 3. Volver.")
            
            circulo = pedir_opcion("Elija una: ", 1, 3)
            if circulo == 3:
                continue
            elif circulo == 1:
                radio = pedir_float("Ingresa radio: ")
            
                area = pi * radio**2
                print("Área:", area)
                
            elif circulo == 2:
                radio = pedir_float("Ingresa radio: ")
                
                perimetro = (2 * pi) * radio
                print("Perímetro:", perimetro)

        elif figura2d == 4:
            print("Elegiste Rombo, ¿Que operación deseas hacer?:\n 1. Área.\n 2. Perímetro.\n 3. Volver.")
            
            rombo = pedir_opcion("Elija una: ", 1, 3)
            if rombo == 3:
                continue
            elif rombo == 1:
                diag_mayor = pedir_float("Ingrese la diagonal mayor: ")
                diag_menor = pedir_float("Ingrese la diagonal menor: ")
                
                area = (diag_mayor * diag_menor)/2
                print("Área:", area)
            
            elif rombo == 2:
                lado = pedir_float("Ingrese lado: ")
                
                perimetro = 4 * lado
                print("Perímetro:", perimetro)
        
        elif figura2d == 5:
            print("Elegiste triángulo rectángulo, ¿Que operación deseas hacer?:\n 1. Área.\n 2. Hipotenusa.\n 3. Volver.")
            
            tri_rec = pedir_opcion("Elija una: ", 1, 3)
            if tri_rec == 3:
                continue
            
            elif tri_rec == 1:
                cateto1 = pedir_float("Ingrese cateto opuesto: ")
                cateto2 = pedir_float("Ingrese cateto adyacente: ")
                
                area = (cateto1 * cateto2) / 2 
                print("Área:", area)
            
            elif tri_rec == 2:
                cateto1 = pedir_float("Ingrese cateto opuesto: ")
                cateto2 = pedir_float("Ingrese cateto adyacente: ")
                
                hipo = (cateto1**2 + cateto2**2) **0.5
                print("Hipotenusa:", hipo)
                
    if opcion == 2:
        print("Figuras 3D:\n 1. Cubo.\n 2. Cono.\n 3. Esfera.\n 4. Cilindro.\n 5. Volver al menu.")
        figura3d = pedir_opcion("Seleccione una figura: ", 1, 5)
    
        if figura3d == 5:
            continue
        elif figura3d == 1:
            print("Elegiste Cubo, ¿Que operación deseas hacer?:\n 1. Área.\n 2. Volumen.\n 3. Volver.")
            
            cubo = pedir_opcion("Elija una: ", 1, 3)
            if cubo == 3:
                continue
            
            elif cubo == 1:
                lado = pedir_float("Ingrese lado: ")

                area = 6 * (lado **2)
                print("Área:", area)
                
            elif cubo == 2:
                lado = pedir_float("Ingrese lado: ")
                
                volumen = lado ** 3
                print("Volumen:", volumen)

        elif figura3d == 2:
            print("Elegiste Cono, ¿Que operación deseas hacer?:\n 1. Área de la base.\n 2. Volumen.\n 3. Volver.")
            
            cono = pedir_opcion("Elija una: ", 1, 3)
            if cono == 3:
                continue
            
            elif cono == 1:
               radio = pedir_float("Ingrese la radio: ")
               area_base = pi *(radio ** 2)
               
               print("Área de la base: ", area_base)
            elif cono == 2:
               radio = pedir_float("Ingrese la radio: ")
               altura = pedir_float("Ingrese la altura: ")
               volumen = (1/3) * pi * (radio **2) * altura
               
               print("Volumen del cono: ", volumen)
            
        elif figura3d == 3:
            print("Elegiste esfera, ¿Que operación deseas hacer?:\n 1. Área.\n 2. Volumen.\n 3. Volver.")
            
            esfera = pedir_opcion("Elija una: ", 1, 3)
            if esfera == 3:
                continue
            
            elif esfera == 1:
                radio = pedir_float("Ingrese la radio: ")
                area = 4 * pi * (radio ** 2)
                
                print("Área: ", area)
                
            elif esfera == 2:
                radio = pedir_float("Ingrese la radio: ")
                
                volumen = (4/3) * pi * (radio ** 3)
                print("Volumen: ", volumen)
        

        elif figura3d == 4:
            print("Elegiste cilíndro, ¿Que operación deseas hacer?:\n 1. Área total.\n 2. Volumen.\n 3. Volver.")
            
            cilindro = pedir_opcion("Elija una: ", 1, 3)
            if cilindro == 3:
                continue
            
            elif cilindro == 1:               
                radio = pedir_float("Ingrese la radio: ")
                altura = pedir_float("Ingrese la altura: ")
                area_total =  2 * pi * radio * (radio + altura)
                
                print("Área total: ", area_total)
            elif cilindro == 2:
                radio = pedir_float("Ingrese la radio: ")
                altura = pedir_float("Ingrese la altura: ")
                volumen = pi *(radio **2) * altura
                
                print("Volumen: ", volumen)
            



           
            





