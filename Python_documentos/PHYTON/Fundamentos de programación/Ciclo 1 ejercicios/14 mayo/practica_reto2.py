#Cantidad de antenas para cubrir cobertura de m2#
import math
zonas=int(input("zonas "))
if zonas>0:
  i=1
  totAnt=0
  while i<=zonas:
    area=float(input("area "))
    antena=int(input("antena "))
    tipo=input("tipo ")
    if antena>=0 and area>0:
      if tipo=="a":
        tA="a"
        Nantena=math.ceil((area-(antena*3000))/800)
        if Nantena<0:
            Nantena=0
        tipoA=Nantena
      elif tipo=="b":
        tB="b"
        Nantena=math.ceil((area-(antena*3000))/52900)
        if Nantena<0:
            Nantena=0
        tipoB=Nantena
      elif tipo=="c":
        tC="c"
        Nantena=math.ceil((area-(antena*3000))/7500)
        if Nantena<0:
            Nantena=0
        tipoC=Nantena
      elif tipo=="d":
        tD="d"
        Nantena=math.ceil((area-(antena*3000))/35600)
        if Nantena<0:
            Nantena=0
        tipoD=Nantena
      elif tipo=="e":
        tE="e"
        Nantena=math.ceil((area-(antena*3000))/49800)
        if Nantena<0:
            Nantena=0
        tipoE=Nantena
    else:
      Nantena=0
    totAnt=totAnt+Nantena
    i=i+1
  print(math.ceil(totAnt))
else:
  Nantena=0
  print(Nantena)
porcA=((tipoA)*100)/totAnt
print((tA), round(porcA,2),"%")
porcB=((tipoB)*100)/totAnt
print((tB), round(porcB,2),"%")
porcC=((tipoC)*100)/totAnt
print((tC), round(porcC,2),"%")
porcD=((tipoD)*100)/totAnt
print((tD), round(porcD,2),"%")
porcE=((tipoE)*100)/totAnt
print((tE), round(porcE,2),"%")
