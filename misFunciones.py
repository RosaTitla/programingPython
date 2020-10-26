def MayorDeDos(numero1, numero2):
    nmasGrande=0
    if numero1 > numero2:
        nmasGrande = numero1
    else:
        nmasGrande = numero2
    return nmasGrande

def mas():
    print('hola')


opc=0
while opc!=4:
    print('\n\n 1 mayor de dos números \n 2 Mayor de 3 números \n 3 Calcular Aumento de sueldo \n 4 Salir')
    opc=int(input('opción'))
    if opc==1:
        n1 = int(input("número: "))
        n2 = int(input("número: "))
        j = MayorDeDos(n1, n2)
        print('El mayor es ', j)
    elif opc==2:
        mas()
    elif opc==4:
        print('programa terminado')
        break
    else:
        print('Opción no válida programa terminado')
        break