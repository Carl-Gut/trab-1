import math

DyT=(input("Num dep y num terr: ")).split(' ')
de=int(DyT[0])
te=int(DyT[1])

# i=1 este no hace falta
while de < 1:
  DyT=input("Num dep y num terr: ").split(' ')
  de=int(DyT[0])
  te=int(DyT[1])
#  i+=1 este no hace falta

# inicializa 2 vectores del tamaño de n, para cant antenas por deptos y cant ant tipo a por deptos
Dep=[]
AntA=[]
Total=0
j = 0
while j < de:
    Dep.append(0)
    AntA.append(0)
    j += 1

# Lees los datos de numDepm aream antenas, tipo
for t in range(te):
  entrada2=input("numDep, area, antenas, tipo: ").split(' ')
  nDep=int(entrada2[0])
  area=float(entrada2[1])
  antenas=int(entrada2[2])
  tipo=(entrada2[3])
  
  # i=1 no hace falta
  while antenas <0:
    entrada2=input("numDep, area, antenas, tipo: ").split(' ')
    nDep=int(entrada2[0])
    area=float(entrada2[1])
    antenas=int(entrada2[2])
    tipo=(entrada2[3])
   # i+=1  no hace falta
  
  
  if nDep<=de and antenas>=0:
      if tipo=="a":
        Nant=math.ceil((area-(antenas*3000))/800)
        Dep[nDep-1]+=Nant
        if Nant<=0:
          Nant=0
        else:
            AntA[nDep-1]+=Nant
      elif tipo=="b":
        Nant=math.ceil((area-(antenas*3000))/52900)
        Dep[nDep-1]+=Nant
      elif tipo=="c":
        Nant=math.ceil((area-(antenas*3000))/7500)
        Dep[nDep-1]+=Nant        
      elif tipo=="d":
        Nant=math.ceil((area-(antenas*3000))/35600)
        Dep[nDep-1]+=Nant
      elif tipo=="e":
        Nant=math.ceil((area-(antenas*3000))/49800)
        Dep[nDep-1]+=Nant
      else:
        Nant=0
  else:
      Nant=0
  Total+=Nant
  t+=1

# print(Dep)
# print(AntA)
# print(Total)

menorValor = min(Dep)
mayorValor = max(Dep)

posicion = 1
for f in Dep:
    if f == menorValor:
        print(posicion, menorValor)
    else:
        posicion += 1

Posicion2 = 1
for g in Dep:
    if g == mayorValor:
        print(Posicion2, mayorValor)
    else:
        Posicion2 += 1

h = 0
while h < de:
    if AntA[h] == 0:
        print(h+1, "0.00 %")
    else:
        print(h+1, str("{0:.2f}".format(float((AntA[h]/Dep[h])*100),2))+'%')
    h += 1
