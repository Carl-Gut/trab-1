prog=int(input("¿Usted está inscrito en el programa, 1 (si) o 2 (no): "))
if prog==2:
    print("Usted debe estar inscrito en el programa para recibir el auxilio")
else: 
    nHijos=int(input("Digite número de hijos: "))
    if nHijos<=0:
        print("Usted no es beneficiario del programa")
    else:
        est=int(input("Digite número de estrato al que pertenece (de 1 a 6): "))
        if est>=4 and est<=6:
            print("El valor del auxilio es de $ 100000")
        elif est==1:
            print("El valor del auxilio es de $ ", (nHijos*200000))
        elif est==2:
            print("El valor del auxilio es de $ ", (nHijos*150000))
        elif est==3:
            print("El valor del auxilio es de $ ", (nHijos*100000))
        else:
            print("Estrato no válido")
