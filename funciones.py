def pedir_float(mensaje):

    valido = False

    while not valido:
        valor = input(mensaje).strip()

        try:
            numero = float(valor)

            if numero < 0:
                print("No se permiten números negativos.")
            else:
                valido = True

        except:
            print("Ingrese un número válido.")

    return numero

def pedir_int(mensaje):

    valido = False

    while not valido:
        valor = input(mensaje).strip()

        try:
            numero = int(valor)

            if numero < 0:
                print("No se permiten números negativos.")
            else:
                valido = True

        except:
            print("Ingrese un número entero válido.")

    return numero

def pedir_opcion(mensaje, minimo, maximo):

    valido = False

    while not valido:

        opcion = pedir_int(mensaje)

        if minimo <= opcion <= maximo:
            valido = True
        else:
            print("Seleccione una opción válida.")

    return opcion