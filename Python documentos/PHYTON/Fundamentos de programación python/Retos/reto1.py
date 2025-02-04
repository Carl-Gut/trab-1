#Cantidad de faltantes para cubrir cobertura de m2#
area=float(input())
antena=int(input())
tipo=input()
if area<=0:
  print("Error en los datos")
elif antena<0:
  print("Error en los datos")
elif tipo!="a" and tipo!="b" and tipo!="c" and tipo!="d" and tipo!="e":
  print("Error en los datos")
else:
  if tipo=="a":
    antenaA=((area-(antena*3000))/800)
    if antenaA<=0:
      antenaA=(antenaA*0)
    print(round(antenaA))
  if tipo=="b":
    antenaB=((area-(antena*3000))/52900)
    if antenaB<=0:
      antenaB=(antenaB*0)
    print(round(antenaB))
  if tipo=="c":
    antenaC=((area-(antena*3000))/7500)
    if antenaC<=0:
      antenaC=(antenaC*0)
    print(round(antenaC))
  if tipo=="d":
    antenaD=((area-(antena*3000))/35600)
    if antenaD<=0:
      antenaD=(antenaD*0)
    print(round(antenaD))
  if tipo=="e":
    antenaE=((area-(antena*3000))/49800)
    if antenaE<=0:
      antenaE=(antenaE*0)
    print(round(antenaE))