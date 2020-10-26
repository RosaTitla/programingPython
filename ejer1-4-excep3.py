#función divide dos números
def divide(n1,n2):
    try:
        d = n1 / n2
    except ZeroDivisionError as error:
        print("No puedes dividir entre cero, lo siento.", error)
    else:
        return d


# funcion que detecta el numero mayor de 3 numeros
def mayorDeTresNumeros(numero1, numero2, numero3):
    nmasGrande = numero1
    if numero2 > nmasGrande:
        nmasGrande = numero2
    if numero3 > nmasGrande:
        nmasGrande = numero3
    return nmasGrande


def calcularAumento(sueldo):
    if sueldo >= 500 and sueldo <= 1000:
        sueldoAumento = sueldo + (sueldo * 0.25)
    elif sueldo > 1000 and sueldo <= 1500:
        sueldoAumento = sueldo + (sueldo * 0.21)
    elif sueldo > 1500:
        sueldoAumento = sueldo + (sueldo * 0.18)
    else:
        sueldoAumento = 0
    return sueldoAumento


opc=0
while opc!=4:
    print('\n\n 1 división de dos números \n 2 Mayor de 3 números \n 3 Calcular Aumento de sueldo \n 4 Salir')
    try:
        opc = int(input('opción: '))
    except Exception as e:
        print("Dato incorrecto", e)
    else:
        if opc==1:
            try:
                n1 = int(input("número: "))
                n2 = int(input("número: "))
            except Exception as e:
                print("datos incorrectos", e)
            else:
                div = divide(n1, n2)
                print('la división es:', div)
        elif opc==2:
            try:
                numero1 = int(input("Ingresa el primer número:"))
                numero2 = int(input("Ingresa el segundo número:"))
                numero3 = int(input("Ingresa el tercer número:"))
            except Exception as e:
                print("datos incorrectos", e)
            else:
                mayor = mayorDeTresNumeros(numero1, numero2, numero3)
                print("El número más grande es:", mayor)
        elif opc==3:
            try:
                sueldo = int(input("Introduce el sueldo actual: "))
            except Exception as e:
                print("datos incorrectos", e)
            else:
                sueldoAum = calcularAumento(sueldo)
                print("El sueldo con aumento es ", sueldoAum)
        else:
            print('programa terminado')


