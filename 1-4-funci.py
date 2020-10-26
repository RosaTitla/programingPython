def square(x):
    print("square")
    return x*x

def g(y):
    print("g")
    return y + 3

print(square(g(2)))


def show_me_numbers(list_of_ints):
    print(10)
    print("Next we'll accumulate the sum")
    accum = 0
    for num in list_of_ints:
        accum = accum + num
    return accum
    print("All done with accumulation!")

show_me_numbers([4,2,3])

def same(cad):
    return cad
#Escriba una función llamada decisión que tome una cadena como entrada y luego verifique el número de caracteres. Si tiene más de 17 caracteres, devuelva "Esta es una cadena larga", si es más corta o tiene 17 caracteres, devuelva "Esta es una cadena corta"
def decision(cad):
    t=len(cad)
    if t>17:
        return 'This is a long string'
    else:
        return 'This is a short string'

#Write a function named num_test that takes a number as input. If the number is greater than 10, the function should return “Greater than 10.” If the number is less than 10, the function should return “Less than 10.” If the number is equal to 10, the function should return “Equal to 10.”

def num_test(t):
    if t>10:
        return 'Greater than 10.'
    elif t<10:
        return 'Less than 10.'
    else:
        return 'Equal to 10.'


def most_common_letter(s):
    frequencies = count_freqs(s)
    return best_key(frequencies)

def count_freqs(st):
    d = {}
    for c in st:
        if c not in d:
             d[c] = 0
        d[c] = d[c] + 1
    return d

def best_key(dictionary):
    ks = dictionary.keys()
    best_key_so_far = list(ks)[0]  # Have to turn ks into a real list before using [] to select an item
    for k in ks:
        if dictionary[k] > dictionary[best_key_so_far]:
            best_key_so_far = k
    return best_key_so_far

print(most_common_letter("abbbbbbbbbbbccccddddd"))

#Escribe dos funciones, una llamada addit y
# otra llamada mult.
# addit toma un número como entrada y suma 5.
# mult toma un número como entrada
# y multiplica esa entrada por lo que sea devuelto por addit,
# y luego devuelve el resultado.
def addit(num):
    return num+5
def mult(nume):
    return nume*addit(2)

c=mult(2)
print(c)

#Assigned to a variable. For example, w = square(3)
#Put in a list. For example, L.append(square(3))
#Put in a dictionary. For example, d[3] = square(3)
#w = square(square(3) + 7) - 5
#print(square(3))
#What will the following code output?
def square(x):
    return x*x

def g(y):
    return y + 3

def h(y):
    return square(y) + 3

print(h(2))

#What will the following code output?
def square(x):
    return x*x

def g(y):
    return y + 3

def h(y):
    return square(y) + 3

print(g(h(2)))
# pasando listas
def double(y):
    y = 2 * y

def changeit(lst):
    lst[0] = "Michigan"
    lst[1] = "Wolverines"

y = 5
double(y)
print(y)

mylst = ['our', 'students', 'are', 'awesome']
changeit(mylst)
print(mylst)

#Puede utilizar el mismo patrón de codificación para
# evitar confundir los efectos secundarios con el
# intercambio de objetos mutables. Para hacer eso,
# haga explícitamente una copia de un objeto y
# pase la copia a la función. Luego, devuelva la copia modificada y vuelva a asignarla a la variable original si desea guardar los cambios. La función de lista incorporada, que toma una secuencia como parámetro y devuelve una nueva lista, trabaja para copiar una lista existente. Para los diccionarios, puede llamar de manera similar a la función dict, pasando un diccionario para obtener una copia del diccionario como valor de retorno.

def changeit(lst):
    lst[0] = "Michigan"
    lst[1] = "Wolverines"
    return lst

mylst = ['106', 'students', 'are', 'awesome']
newlst = changeit(list(mylst))
print(mylst)
print(newlst)

#Write a function that will return the number of digits in an integer

def numDigits(n):
    # your code here
    if n>=1 and n<=9:
        return 1
    elif n>=10 and n<=99:
        return 2
    elif n>=100 and n<=999:
        return 3
print(numDigits(450))

def reverse(astring):
    # your code here
    lista=list(astring)
    #print(lista)
    return lista.reverse()

print(reverse('rosa'))







