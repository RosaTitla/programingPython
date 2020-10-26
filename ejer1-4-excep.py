#n1=int(input("número: "))
#n2=int(input("número: "))



def divide(n1,n2):
    try:
        d = n1 / n2
    except ZeroDivisionError as error:
        print("No puedes dividir entre cero, lo siento.")
    else:
        return d
    finally:
        print("la función terminó")
c=0
while c<2:
    try:
        n1=int(input("número: "))
        n2=int(input("número: "))
    except ValueError as e:
        print("Debes ingresar un numero.", e)
    else:
        div = divide(n1, n2)
        c += 1
        print('la división es:',div)
    finally:
        print("el programa terminó")
