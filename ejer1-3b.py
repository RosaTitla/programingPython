a="Rosario"
b="Titla"
c=a+b
print(c)

z=int(input("Cuántas calificaciones"))
for i in range(z):
    calif=float(input('calificación'))


for i in range(z):
    print(i, end=" ") # salidas: 0 1 2






for i in range(6, 1, -2):
    print(i, end=" ") # salidas: 6, 4, 2

for i in range (2):
    print(i)


for i in range(5):
    print("El valor de i es actualmente", i)

#Es posible en forma descendente, cuando el incremento es negativo
for i in range (10,1, -1):
    print("El valor de i es actualmente descende", i)

# break - ejemplo
print("La instrucción de ruptura:")
for i in range(1,6):
    if i == 3:
        break
    print("Dentro del ciclo.", i)
print("Fuera del ciclo.")

# continue - ejemplo
print("\nLa instrucción continue:")
for i in range(1,6):
    if i == 3:
        continue
    print("Dentro del ciclo.", i)
print("Fuera del ciclo.")
