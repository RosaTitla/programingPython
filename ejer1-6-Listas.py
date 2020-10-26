letras=[]
c=0
for x in range(3):
    letra=input('letra')
    letras.append(letra)
    if letras[x]=='a':
        c+=1

print(letras)
print('total de letras a',c)


lista1=[] # creando una lista vacía
lista1.append(480) #agrega el número 480 a la lista1
print(lista1)

#solicitamos al usuario del programa
# el total de elementos que insertará en la lista
totElem=int(input('Total de elementos'))

#bucle para agregar a la lista los números dados por el usario
for i in range(totElem):
    numero=int(input('número:'))
    lista1.append(numero)
print(lista1)

#obtener el índice (posición) en el que se encuentra un elemento
print('el elemento 10 se encuentra en la posición: ',lista1.index(10))

#la función len calcula la longitud o tamaño de la lista
longitud=len(lista1)
print('longitud de la lista: ',longitud)

#bucle para sumar los elementos de la lista1
suma=0
for i in range(longitud):
    suma=suma+lista1[i]
print('suma total: ',suma)

#almacenar los números generados por range() en la lista2
#recuerda que range genera un número y lo almacena en la var i
lista2=[]
for i in range(3,10):
    lista2.append(i)
print(lista2)

#borrar el elemento 10 de la lista
lista1.remove(10)
print('elemento 10 borrado')
print(lista1)

#otro método para borrar el elemento de la lista
# es del y borrará el elemento que se encuentra en la posición 2
del lista1[2]
print('elemento de la posición 2 borrado')
print(lista1)

#insert (posición,dato)
lista1.insert(0,500)
print(lista1)

# otra forma para recorrer la lista1 por sus elementos
for k in lista1:
    cubo=k**3
    print('cubo:',cubo)

#ordenar una lista en forma ascendente
lista1.sort()
print(lista1)

#ordenar la lista en forma descendente
lista1.reverse()
print(lista1)

#copiartodo el contenido de la lista1 a lista2
lista2=[]
lista2=lista1[:]
print(lista2)
lista3=[]
#realiza una copia de lista1 a lista3
# desde el elemento que se encuentra en la posición 2
# hasta el elemento que se encuentra la posición 4
lista3=lista1[2:5]
print(lista3)

#El siguiente ejemplo
# creará una lista llamada listaCuadrados que almacenará
# los valores generados por range (desde el 3 hasta el 9)
# y con ayuda del for elevará al cuadrado cada numero generado por el range
listaCuadrados = [x ** 2 for x in range(3,10)]
print(cuadrados)

dos = [2 ** i for i in range(8)]
print(dos)
#El fragmento hace una lista
# con solo los elementos impares de la lista cuadrados.
probabilidades = [x for x in cuadrados if x % 2 != 0]
print(probabilidades)

#Este es un ejemplo de una lista de comprensión:
# el código siguiente crea una lista de cinco elementos
# con los primeros cinco números naturales elevados a la potencia de 3
cubos = [num ** 3 for num in range (5)]
#listas dentro de una lista

