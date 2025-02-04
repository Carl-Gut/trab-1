import math

DyT=input().split(' ')
de=int(DyT[0])
te=int(DyT[1])

while de<1:
  DyT=input().split(' ')
  de=int(DyT[0])
  te=int(DyT[1])

Dep=[]
AntA=[]
Total=0
j=0
while j < de:
  Dep.append(0)
  AntA.append(0)
  j+=1

for t in range(te):
  entrada2=input().split(' ')
  nDep=int(entrada2[0])
  area=float(entrada2[1])
  antenas=int(entrada2[2])
  tipo=(entrada2[3])
  
  while antenas<0:
    entrada2=input().split(' ')
    nDep=int(entrada2[0])
    area=float(entrada2[1])
    antenas=int(entrada2[2])
    tipo=(entrada2[3])
  
  if nDep<=de and antenas>=0:
    if tipo=="a":
      Nant=math.ceil((area-(antenas*3000))/800)
      if Nant<0:
        Nant=0
      else:
        AntA[nDep-1]+=Nant
      Dep[nDep-1]+=Nant
    elif tipo=="b":
      Nant=math.ceil((area-(antenas*3000))/52900)
      if Nant<0:
        Nant=0
      Dep[nDep-1]+=Nant
    elif tipo=="c":
      Nant=math.ceil((area-(antenas*3000))/7500)
      if Nant<0:
        Nant=0
      Dep[nDep-1]+=Nant        
    elif tipo=="d":
      Nant=math.ceil((area-(antenas*3000))/35600)
      if Nant<0:
        Nant=0
      Dep[nDep-1]+=Nant
    elif tipo=="e":
      Nant=math.ceil((area-(antenas*3000))/49800)
      if Nant<0:
        Nant=0
      Dep[nDep-1]+=Nant
  Total+=Nant
  t+=1

menorValor=min(Dep)
mayorValor=max(Dep)

posicion = 1
for f in Dep:
  if f == menorValor:
    print(posicion, menorValor)
  else:
    posicion += 1

Posicion2=1
for g in Dep:
  if g == mayorValor:
    print(Posicion2, mayorValor)
  else:
    Posicion2 += 1

h = 0
while h < de:
  if AntA[h] == 0:
    print(h+1, "0.00%")
  else:
    print(h+1, "{0:.2f}".format(AntA[h]/Dep[h]*100)+"%")
  h += 1
