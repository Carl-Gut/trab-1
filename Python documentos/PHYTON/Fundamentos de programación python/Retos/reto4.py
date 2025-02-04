import math

def convert_type_to_int(type_):
  type_list = ['a', 'b', 'c', 'd', 'e']
  return type_list.index(type_)

def list_divide(a, b):
  c = []
  for i in range(len(a)): 
    c.append(0) if b[i] == 0 else c.append(a[i] / b[i])
  return c

def get_elem_index(a, elem=None):
    if elem == 'min':
        return min(a), a.index(min(a))
    elif elem == 'max':
        return max(a), a.index(max(a))
    else:
        return elem, a.index(elem)

DyT=input().split(' ')
de=int(DyT[0])
te=int(DyT[1])

while de<1:
  DyT=input().split(' ')
  de=int(DyT[0])
  te=int(DyT[1])

Tipo_antena=[]
for i in range (de):
  Tipo_antena.append([0 for i in range(5)])

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
  
  if nDep<=de and nDep>0:
    if tipo=="a":
      Tipo_antena[nDep-1][convert_type_to_int(tipo)] += max(0, math.ceil((area- 3000*antenas)/800))
    elif tipo=="b":
      Tipo_antena[nDep-1][convert_type_to_int(tipo)] += max(0, math.ceil((area- 3000*antenas)/52900))
    elif tipo=="c":
      Tipo_antena[nDep-1][convert_type_to_int(tipo)] += max(0, math.ceil((area- 3000*antenas)/7500))    
    elif tipo=="d":
      Tipo_antena[nDep-1][convert_type_to_int(tipo)] += max(0, math.ceil((area- 3000*antenas)/35600))
    elif tipo=="e":
      Tipo_antena[nDep-1][convert_type_to_int(tipo)] += max(0, math.ceil((area- 3000*antenas)/49800))

types = ["a", "b", "c", "d", "e"]
for i in range(de):
    min_, index_min = get_elem_index(Tipo_antena[i], elem='min')
    max_, index_max = get_elem_index(Tipo_antena[i], elem='max')

    print(i + 1)
    print(sum(Tipo_antena[i]))  
    print(types[index_min], min_)
    print(types[index_max], max_)

for i in range(len(types)):  
    actual_type = [t_ant[i] for t_ant in Tipo_antena]
    min_, index_min = get_elem_index(actual_type, elem='min')
    max_, index_max = get_elem_index(actual_type, elem='max')

    print(index_min + 1, types[i], min_)
    print(index_max + 1, types[i], max_)


'''
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
'''