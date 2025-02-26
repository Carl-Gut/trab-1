import math
n=int(input('Ingrese el primer Numero: '))
m=int(input('Ingrese el segundo Numero: '))
resto=int(n % m)
cociente=math.trunc(n/m)
print('con los numeros ',n,' y',m,' da resultado como resto', resto,' y cociente ', cociente)