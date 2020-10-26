#ingreso=float(input("Ingrese el ingreso anual:"))

#
# Coloca tu código aquí.
#



def  sat():
    ing=float(input("ingresos"))
    if ing<85528:
        impuesto=(ing*.18)-556.02
    else:
        impuesto=14839.02+(ing-85528)*.32
        impuesto=round(impuesto, 1)
    print("El impuesto es: ", impuesto, "pesos")

from math import sqrt,fabs
cont1,cont2,cont3,cont4=0

def operaciones(n):
    cuadrado = n**2
    cubo = n**3
    raiz = sqrt(n)
    valor = fabs(n)
    modulo = n%4
    return cuadrado, cubo, raiz, valor, modulo

n=int(input('numero'))

c, cu, r, v, m = operaciones(n)
print("El cuadro de",n,"es igual a:",c)
print("El cubo de",n,"es igual a:",cu)
print("La raíz cuadrada de",n,"es igual a:",r)
print("El valor absoluto de",n,"es igual a:",v)
print("El modulo 4 de",n,"es igual a",m)