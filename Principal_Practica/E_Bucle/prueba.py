cantinv=int(input("Escriba la inversion: "))
interes=float(input("Escriba el interes: "))
cantaños=int(input("Escriba los años: "))
for i in range(1,cantaños+1,1):
     total1=(cantinv*(interes/100))
     total=total+total1
     print("Año ",i,"valor obtenido: ",total)