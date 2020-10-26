# en c#  for(int i = 0; i < 10; i++)
#3,4,5,6,7,8
#t=int(input('total'))
#break
for j in range(6):
    if j==3:
        break
    print('el valor de j es', j)

ingresos=float(input('ingresos'))
if ingresos<85528:
    impuesto=(ingresos*.18)-556.02
else:
    impuesto=(ingresos-85528)*.32+14839.02

salario=float(input('salario'))
opc=int(input('1. Cuota,  2 Porcentaje'))
if opc==1:
   cuota=float(input('cuota'))
   sar=salario-cuota
if opc==2:
   porcentaje=int(input('que porcentaje'))
   sar=salario*(porcentaje/100)

cant=int(input('cantidad'))
precio=float(input('precio'))
marca=input('marca')
if marca=='bic':
    desc=(cant*precio)*.18
    stot=cant*precio-desc
elif marca=='pelikan':
    desc = (cant * precio) * 0.16
    stot = cant * precio - desc
t=stot+(stot*.16)


n1=int(input('num'))
n2=int(input('num'))
n3=int(input('num'))

if n1==n2==n3:
    print('iguales')
elif n1!=n2==n3:
    print ('n1 dif')
