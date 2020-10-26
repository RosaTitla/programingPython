def mayor2num(n1,nu2):
    if numero1 > numero2:
        nmasGrande = numero1
    else:
        nmasGrande = numero2
    return nmasGrande


#leer dos números y encuentra el mayor
numero1 = int (input("Ingresa el primer número:"))
numero2 = int (input("Ingresa el segundo número:"))

z=mayor2num(numero1,numero2)
print("el mayor es",z)

#elegir el número más grande
if numero1> numero2:
    nmasGrande = numero1
else:
    nmasGrande = numero2
print("El número más grande es:", nmasGrande)



# lee tres números y encontremos el mayor de los tres números
numero1 = int (input("Ingresa el primer número:"))
numero2 = int (input("Ingresa el segundo número:"))
numero3 = int (input("Ingresa el tercer número:"))
#asumimos temporalmente que el primer número
#es el más grande lo verificaremos pronto
nmasGrande = numero1
#comprobamos si el segundo número es más grande que el mayor número actual
#y actualiza el número más grande si es necesario
if numero2 > nmasGrande:
    nmasGrande = numero2
#comprobamos si el tercer número es más grande que el mayor número actual
#y actualiza el número más grande si es necesario
if numero3 > nmasGrande:
    nmasGrande = numero3
#imprimir el resultado
print("El número más grande es:", nmasGrande)






#programa que presente un menú de opciones
# y realiza la operacion segun la opción elegida
print('1 suma \n 2 Resta \n 3 multiplicación \n 4 división \n')
opc=int(input('opción'))
numero1 = int (input("Ingresa el primer número:"))
numero2 = int (input("Ingresa el segundo número:"))
if opc==1:
    res=numero1+numero2
    operacion="suma"
elif opc==2:
    res = numero1 - numero2
    operacion='resta'
elif opc==3:
    res = numero1 * numero2
    operacion='multiplicación'
elif opc==4:
    res = numero1 / numero2
    operacion='división'
else:
    res=0
    operacion='operación no válida'
print(operacion, '\t',res)

