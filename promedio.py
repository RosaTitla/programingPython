
#n=int(input('total'))
min=1000
max=0
sumaPuntos=0
for k in range(5):
    punt=int(input('puntos contaminantes'))
    sumaPuntos=sumaPuntos+punt
    if punt<min:
        min=punt
    if punt>max:
        max=punt

prom=sumaPuntos/5
print('minimo',min)
print('max',max)




