#programa que dado como dato el sueldo de un trabajador,
# calcule su aumento según el siguiente criterio:
#Si el sueldo es menor que $1000 se le aumentara un 25%.
#Si el sueldo es mayor que $1000 pero menor que $1500
# se le aumentara el 21% en caso contrario se le aumentara el 18%.
#sueldoAumento=0
cont=0
tot=int(input('total de empleados o escribe 0 para terminar'))
while tot!=0:
    #cont=cont+1
    sueldo = float(input("Introduce el sueldo actual: ") )
    if sueldo>=1 and sueldo<=1000:
        sueldoAumento=sueldo+(sueldo*0.25)
    elif sueldo>1000 and sueldo<=1500:
        sueldoAumento=sueldo+(sueldo*0.21)
    elif sueldo>1500:
        sueldoAumento=sueldo+(sueldo*0.18)
    else:
        sueldoAumento=0
    sueldoAumento=round(sueldoAumento,1)
    print("El sueldo con aumento es ", sueldoAumento)
    tot = int(input('total de empleados o escribe 0 para terminar'))

