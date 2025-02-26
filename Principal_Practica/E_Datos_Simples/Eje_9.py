cantinv=float(input('Ingresar valor Invertir:'))
intanual=float(input('Ingresar interes:'))
intanual=intanual/100
añoscant=int(input('Ingresar años: '))
intxaño=float(cantinv*intanual)
ganancia=round(float(intxaño*añoscant))
print(' Las ganancias son: ', ganancia)