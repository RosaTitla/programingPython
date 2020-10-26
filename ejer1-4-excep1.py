try:
    i = int(input("numero"))
    #a=4/i
except Exception as e:
    print("ocurrió un error:",e)


# class miException(Exception):
#     def __init__(self, value):
#         self.value = value
#     def __str__(self):
#         return (self.value)
#
#
# for x in range(2):
#     try:
#         i = float(input("Escribe un número positivo"))
#         if i<=0:
#             raise miException("")
#     except miException:
#         print("El número no es positivo")
# print("assert")
# i = float(input("Escribe un número positivo"))
# assert i >= 0  #si el resultado de la condicion es falsa se genera la excepcion
# print("El número no es positivo")
#
# import math
#
# x = float(input("Ingresa un numero: "))
# assert x >= 0.0
#
# x = math.sqrt(x)
#
# print(x)




