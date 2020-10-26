
#base elevada a potencia para N número de veces

contador = 0
tot = int(input("Introduce total de números"))

while contador < tot:
    contador = contador + 1
    base=int(input("base: "))
    expo=int(input("exponente: "))
    potencia=pow(base,expo)
    print(base, "elevado a", expo,"es",potencia)



# programa que dado como dato el sueldo de un trabajador,
# calcule su aumento según el siguiente criterio:
    # Si el sueldo es menor que $1000 se le aumentara un 25%.
    # Si el sueldo es mayor que $1000 pero menor que $1500
    # se le aumentara el 21% en caso contrario se le aumentara el 18%.
    # sueldoAumento=0
contador = 0
tot = int(input("Introduce total de empleados"))
while contador < tot:
    contador = contador + 1
    sueldo = int(input("Introduce el sueldo actual: "))
    if sueldo >= 1 and sueldo <= 1000:
        sueldoAumento = sueldo + (sueldo * 0.25)
    elif sueldo > 1000 and sueldo <= 1500:
        sueldoAumento = sueldo + (sueldo * 0.21)
    elif sueldo > 1500:
        sueldoAumento = sueldo + (sueldo * 0.18)
    else:
        sueldoAumento = 0
    print("El sueldo con aumento es ", sueldoAumento)

# programa que lee una secuencia de números
# y cuenta cuántos números son pares y cuántos son impares
# programa termina cuando se ingresa cero
numerosImpares = 0
numerosPares = 0
# lee el primer número
numero = int (input ("Introduce un número o escriba 0 para terminar:"))
# 0 termina la ejecución
while numero != 0:
    # verificar si el número es impar
    if numero % 2 == 1:
        # aumentar el contador de números impares numerosImpares=numerosImpares+1
        numerosImpares += 1
    else:
        # aumentar el contador de números pares   numerosPares=numerosPares+1
        numerosPares += 1
    # lee el siguiente número
    numero = int (input ("Introduce un número o escriba 0 para terminar:"))
# imprimir resultados
print("Números impares: ", numerosImpares)
print("Números pares: ", numerosPares)
