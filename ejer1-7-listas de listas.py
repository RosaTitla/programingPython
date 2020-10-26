tablero  = []
EMPTY =0
for i in range(8):
    fila = [EMPTY for i in range(8)]
    tablero.append(fila)
    print(fila)

print("matriz diagonal")
for i in range(8):
    for j in range(8):
        if i==j:
            tablero[i][j]=1
print(tablero)

print("matriz diagonal 2")
for i in range(8):
    [1 for j in range(8) if i==j]
print(tablero)

for row in tablero:
    print(row)

for j in range(1,3):
    print(j)

listaMuestra = ["A", "B", "C", "D", "E"]
nuevaLista = listaMuestra[0:-3]
print(nuevaLista) # salida: ['C', 'D']


l1 = ["A", "B", "C"]
l2 = l1
l3 = l2

print (l1)
print (l2)
print (l3)
del l1[0]
del l2

print(l3)
temps = [[0.0 for h in range (24)] for d in range (31)]
print(temps)