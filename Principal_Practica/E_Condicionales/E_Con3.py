primerN = int(input('Ingrese el 1 Num:'))
segN = int(input('Ingrese el 2 Num:'))
res = int(primerN % segN)
if res == 0:
    print('Error de valores')
else:
    print('el resultado es: ', res)