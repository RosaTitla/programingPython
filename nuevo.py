#for i=0; i<5; i++
#0,1,2,3
tot=int(input('total de numeros'))
for i in range(tot):
    print('valor',i)
    nombre=input('nombre')

for j in range(10,0,-1):
    print('valor j',j)
    if j==5:
        break


suma=0
promMax=0
for x in range(tot):
    matricula=input(('matricula'))
    suma=0
    for y in range(5):
        calif=int(input('calificacion'))
        suma=suma+calif
    print('suma',suma)
    prom=suma/5
    print('promedio',prom)
    if prom>promMax:
        promMax=prom
        matriculaMax=matricula

print('prom max',promMax)
print('matricula',matricula)

