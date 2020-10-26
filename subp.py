def sumar(n1,n2):
    s = 1 / 2 * (n1 + n2)
    return s



#funcion ejercicio 2



#funcion para ejercicio 3
opc=0
while opc!=4:
    print('\n\n 1 suma \n 2 Mayor de 3 números \n 3 Calcular Aumento de sueldo \n 4 Salir')
    opc=int(input('opción'))
    if opc==1:
        n1 = int(input('numero 1'))
        n2 = int(input('numero 2'))

        r = sumar(n1, n2)
        print("resultado", r)




