print("raising")
j = float(input("Escribe un número negativo"))
if j>0:
    raise Exception("no es negativo")
else:
    k=10-j
    print("total", k)
print ("programa 1 terminado")

#z=1+5+"tres"

print("raising 2")
try:
    j = float(input("Escribe un número negativo"))
    if j>0:
        raise Exception("no es negativo")
    else:
        k = 10 - j
        print("total", k)
except Exception as error:
    print(error)
print ("programa 2 terminado")