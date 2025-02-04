#Cantidad de faltantes para cubrir cobertura de m2#
import math
zonas=int(input("zonas "))
if zonas>0:
  i=1
  totAnt=0
  sumA=0
  while i<=zonas:
    area=float(input("area "))
    antena=int(input("antena "))
    tipo=input("tipo ")
    if antena>=0 and area>0:
      if tipo=="a": 
        Nantena=math.ceil((area-(antena*3000))/800)
        if Nantena<0:
          Nantena=0
        NantA=float(Nantena)
      elif tipo=="b":
        Nantena=math.ceil((area-(antena*3000))/52900)
        if Nantena<0:
          Nantena=0
      elif tipo=="c":
        Nantena=math.ceil((area-(antena*3000))/7500)
        if Nantena<0:
          Nantena=0
      elif tipo=="d":
        Nantena=math.ceil((area-(antena*3000))/35600)
        if Nantena<0:
          Nantena=0
      elif tipo=="e":
        Nantena=math.ceil((area-(antena*3000))/49800)
        if Nantena<0:
          Nantena=0
    else:
      Nantena=0
    totAnt+=Nantena
    i=i+1
  print(math.ceil(totAnt))
  sumA+=NantA
  
else:
  Nantena=0
  print(Nantena)
