#calcular el cuadrado de los primeros 10 numeros
for j in range(10):
    cuadrado=j*j
    print("el cuadrado de", j, "es", cuadrado)
#calcular el total a pagar por la compra de productos
#como no sabemos cuántos clientes llegarán a comprar
#necesitaremos finalizar el programa con break y una clave de fin
print("Escribe -1 para finalizar el programa")
while True:
    precio = float (input ("Precio: "))
    if precio == -1: #condición para romper el bucle
        break    #para romper el bucle
    cant=int(input("Cantidad: "))
    marca=input('marca: ')
    subtot=precio*cant
    if marca=='stanley':
        desc=subtot*.10
        tot=subtot-desc
    else:
        tot=subtot-0
    tot=round(tot,1)
    print('total a pagar', tot)


