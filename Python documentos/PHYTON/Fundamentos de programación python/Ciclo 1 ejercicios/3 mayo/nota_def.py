print("Nota definitiva estudiantes ciclo 1")
reto1=float(input("Digite nota del reto 1: "))
reto2=float(input("Digite nota del reto 2: "))
reto3=float(input("Digite nota del reto 3: "))
reto4=float(input("Digite nota del reto 4: "))
reto5=float(input("Digite nota del reto 5: "))
ingles=float(input("Digite nota de inglés: "))
if reto1 and reto2 and reto3 and reto4 and reto5 and ingles >=0 and reto1 and reto2 and reto3 and reto4 and reto5 and ingles <=5:
    not_fin=float((reto1*0.10)+(reto2*0.10)+(reto3*0.20)+(reto4*0.20)+(reto5*0.20)+(ingles*0.20))
    print("Su nota definitiva para el ciclo 1 es: "+str(round(not_fin,2)))
else:
    print("Las notas deben ser en rango de 0 a 5")
    
if not_fin>=3:
    print("Usted ganó la asignatura")
else:
    print("Usted no ganó la asignatura")

if not_fin<=5 and not_fin>=4.5:
    print("Su calificación fue Excelente")
elif not_fin<4.5 and not_fin>=3.9:
    print("Su calificación fue Muy buena")
elif not_fin<3.9 and not_fin>3.5:
    print("Su calificación fue Buena")
elif not_fin<=3.5 and not_fin>=3:
    print("Su calificación fue Normal")
else:
    print("Debe recuperar")
