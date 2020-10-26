#función genera números de mayor a menor
#Es posible en forma descendente, cuando el incremento es negativo
def generarNumeros():
    for i in range (10,1, -1):
        print("El valor de i es actualmente descendente", i)

#invocamos la función para que se ejecute
generarNumeros()

def piepulgam(pie, pulgada = 0.0):
    return pie * 0.3048 + pulgada * 0.0254

print(piepulgam(6))


#función divide dos números
def divide(n1,n2):
    d = n1 / n2
    return d

n1=int(input("número: "))
n2=int(input("número: "))
#invocamos a la función divide
# para que se ejecute y
# retorne el resultado
#el resultado lo almacena en la variable div
div=divide(n1,n2)
print('la división es:',div)
#funcion que detecta el numero mayor de 3 numeros dados por el usuario
def mayorDeTresNumeros(numero1, numero2, numero3):
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
    return nmasGrande

# lee tres números y encontremos el mayor de los tres números
numero1 = int (input("Ingresa el primer número:"))
numero2 = int (input("Ingresa el segundo número:"))
numero3 = int (input("Ingresa el tercer número:"))
mayor=mayorDeTresNumeros(numero1,numero2,numero3)
print("El número más grande es:", mayor)





#funcion CalcularAumento que dado como dato el sueldo de un trabajador,
# calcule su aumento según el siguiente criterio:
#Si el sueldo es menor que $1000 se le aumentara un 25%.
#Si el sueldo es mayor que $1000 pero menor que $1500
# se le aumentara el 21% en caso contrario se le aumentara el 18%.

def calcularAumento(sueldo):
    if sueldo>=500 and sueldo<=1000:
        sueldoAumento=sueldo+(sueldo*0.25)
    elif sueldo>1000 and sueldo<=1500:
        sueldoAumento=sueldo+(sueldo*0.21)
    elif sueldo>1500:
        sueldoAumento=sueldo+(sueldo*0.18)
    else:
        sueldoAumento=0
    return sueldoAumento

sueldo = int(input("Introduce el sueldo actual: ") )
sueldoAum=calcularAumento(sueldo) #invocamos a la función y le enviamos el sueldo
print("El sueldo con aumento es ", sueldoAum)



opc=0
while opc!=4:
    print('\n\n 1 división de dos números \n 2 Mayor de 3 números \n 3 Calcular Aumento de sueldo \n 4 Salir')
    opc=int(input('opción'))
    if opc==1:
        n1 = int(input("número: "))
        n2 = int(input("número: "))
        # invocamos a la función divide para que se ejecute y
        # retorne el resultado que se almacena en la variable div
        div = divide(n1, n2)
        print('la división es:', div)
    elif opc==2:
        numero1 = int(input("Ingresa el primer número:"))
        numero2 = int(input("Ingresa el segundo número:"))
        numero3 = int(input("Ingresa el tercer número:"))
        mayor = mayorDeTresNumeros(numero1, numero2, numero3)
        print("El número más grande es:", mayor)
    elif opc==3:
        sueldo = int(input("Introduce el sueldo actual: "))
        sueldoAum = calcularAumento(sueldo)  # invocamos a la función y le enviamos el sueldo
        print("El sueldo con aumento es ", sueldoAum)
    else:
        print('programa terminado')


def imc(peso, altura):
    if altura < 1.0 or altura > 2.5 or \
            peso < 20 or peso > 200:
        return

    return peso / altura ** 2


print(imc(352.5, 1.65))

def square(x):
    y = x * x
    return y

print(square(5) + square(5))

def square(x):
    y = x * x
    return y

print(square(square(2)))

def cyu2(s1, s2):
    x = len(s1)
    y = len(s2)
    return x-y

z = cyu2("Yes", "no")
if z > 0:
    print("First one was longer")
else:
    print("Second one was at least as long")