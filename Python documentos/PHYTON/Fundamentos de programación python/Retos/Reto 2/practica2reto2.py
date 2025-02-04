#Cantidad de antenas para cubrir cobertura de m2#
import math
zonas=int(input("zonas "))
if zonas>0:
  i=1
  totAnt=0
  NantA=0
  NantB=0
  NantC=0
  NantD=0
  NantE=0
  while i<=zonas:
    area=float(input("area "))
    antena=int(input("antena "))
    tipo=input("tipo ")
    if antena>=0 and area>0:
      if tipo=="a":
        Nant=math.ceil((area-(antena*3000))/800)
        NantA+=Nant
      if tipo=="b":
        Nant=math.ceil((area-(antena*3000))/52900)
        NantB+=Nant
      if tipo=="c":
        Nant=math.ceil((area-(antena*3000))/7500)
        NantC+=Nant
      if tipo=="d":
        Nant=math.ceil((area-(antena*3000))/35600)
        NantD+=Nant
      if tipo=="e":
        Nant=math.ceil((area-(antena*3000))/49800)
        NantE+=Nant
    else:
      Nant=0
    totAnt=totAnt+Nant
    i=i+1
else:
  Nant=0
  print(Nant)
  print("a " + "0.00%")
  print("b " + "0.00%")
  print("c " + "0.00%")
  print("d " + "0.00%")
  print("e " + "0.00%")

print(math.ceil(totAnt))
porA=float(NantA*100)/totAnt
porB=float(NantB*100)/totAnt
porC=float(NantC*100)/totAnt
porD=float(NantD*100)/totAnt
porE=float(NantE*100)/totAnt
print("a {:.2f}".format(porA)+"%")
print("b {:.2f}".format(porB)+"%")
print("c {:.2f}".format(porC)+"%")
print("d {:.2f}".format(porD)+"%")
print("e {:.2f}".format(porE)+"%")
