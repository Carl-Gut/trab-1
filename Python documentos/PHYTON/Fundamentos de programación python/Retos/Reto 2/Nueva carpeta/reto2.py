#Cantidad de antenas para cubrir cobertura de m2#
import math

zonas=int(input(" "))
if zonas>=0:
  i=1
  totAnt=0
  NantA=0
  NantB=0
  NantC=0
  NantD=0
  NantE=0
  while i<=zonas:
    area=float(input(" "))
    antena=int(input(" "))
    tipo=input(" ")
    if antena>=0 and area>0:
      if tipo=="a":
        Nant=math.ceil((area-(antena*3000))/800)
        if Nant<=0:
          Nant=0
        NantA+=Nant
      elif tipo=="b":
        Nant=math.ceil((area-(antena*3000))/52900)
        if Nant<=0:
          Nant=0
        NantB+=Nant
      elif tipo=="c":
        Nant=math.ceil((area-(antena*3000))/7500)
        if Nant<=0:
          Nant=0
        NantC+=Nant
      elif tipo=="d":
        Nant=math.ceil((area-(antena*3000))/35600)
        if Nant<=0:
          Nant=0
        NantD+=Nant
      elif tipo=="e":
        Nant=math.ceil((area-(antena*3000))/49800)
        if Nant<=0:
          Nant=0
        NantE+=Nant   
      else:
        Nant=0
      if Nant<=0:
        Nant=0  
    else:
      Nant=0
    totAnt+=Nant
    i=i+1    
else:
  Nant=0

if totAnt<=0:
  totAnt=0

print(math.ceil(totAnt))
porA=float(NantA*100)/math.ceil(totAnt)
porB=float(NantB*100)/math.ceil(totAnt)
porC=float(NantC*100)/math.ceil(totAnt)
porD=float(NantD*100)/math.ceil(totAnt)
porE=float(NantE*100)/math.ceil(totAnt)
print("a {:.2f}".format(porA)+"%")
print("b {:.2f}".format(porB)+"%")
print("c {:.2f}".format(porC)+"%")
print("d {:.2f}".format(porD)+"%")
print("e {:.2f}".format(porE)+"%")
