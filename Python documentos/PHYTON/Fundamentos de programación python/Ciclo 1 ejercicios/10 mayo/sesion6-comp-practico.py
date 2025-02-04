#menú 3 opciones
opc=int(input("¡Qué quieres que realice?\nEscribe 1 para mostrar dígito mayor\nEscriba 2 para formar tercer número\nEscriba 3 para formar mayor número de cifras: "))
if opc==1:
    print("Al escribir un número de 4 cifras, le diré cuál es el mayor, y sí es par o impar")
    numOp1=int(input("Escribe un número positivo de 4 dígitos: "))
    dig1=numOp1//1000
    dig1_1=numOp1%1000
    dig2=dig1_1//100
    dig2_2=dig1_1%100
    dig3=dig2_2//10
    dig4=dig2_2%10
    if numOp1 in range(0000,10000):
        if dig1>=dig2 and dig1>=dig3 and dig1>=dig4 and dig1%2==0:
            print(f"El dígito {dig1} es el mayor y es par")
        elif dig1>=dig2 and dig1>=dig3 and dig1>=dig4 and dig1%2!=0:
            print(f"El dígito {dig1} es el mayor y es impar")
        elif dig2>=dig1 and dig2>=dig3 and dig2>=dig4 and dig2%2==0:
            print(f"El dígito {dig2} es el mayor y es par")
        elif dig2>=dig1 and dig2>=dig3 and dig2>=dig4 and dig2%2!=0:
            print(f"El digito {dig2} es el mayor y es impar")
        elif dig3>=dig1 and dig3>=dig2 and dig3>=dig4 and dig3%2==0:
            print(f"El digito {dig3} es el mayor y es par")
        elif dig3>=dig1 and dig3>=dig2 and dig3>=dig4 and dig3%2!=0:
            print(f"El dígito {dig3} es el mayor y es impar")
        elif dig4>=dig1 and dig4>=dig2 and dig4>=dig3 and dig4%2==0:
            print(f"El dígito {dig4} es el mayor y es par")
        elif dig4>=dig1 and dig4>=dig2 and dig4>=dig3 and dig4%2!=0:
            print(f"El dígito {dig4} es el mayor y es impar")
    else:
        print("Número fuera de rango")
elif opc==2:
    print("De 2 números de 3 cifras que escriba, se creará un nuevo número \ncon el mayor del primer número y el menor del segundo")
    n1Op2=int(input("Escriba un número de 3 dígitos: "))
    n2Op2=int(input("Escriba otro número de 3 dígitos: "))
    if n1Op2 and n2Op2 in range(000,1000):
        cen1=n1Op2//100
        cen1_1=n1Op2%100
        dec1=cen1_1//10
        un1=cen1_1%10
        cen2=n2Op2//100
        cen2_2=n2Op2%100
        dec2=cen2_2//10
        un2=cen2_2%10
        maxi=max(cen1,dec1,un1)
        mini=min(cen2,dec2,un2)
        print(f"El nuevo número formado es {maxi}{mini}")
    else:
        print("Número fuera de rango")
elif opc==3:
    print("Escriba un número de 3 cifras y le daré el número mayor posible entre sus cifras")
    num3=int(input("Escriba un número de 3 cifras: "))
    if num3 in range(000,1000):
        cen3=num3//100
        cen3_1=num3%100
        dec3=cen3_1//10
        un3=cen3_1%10
        may=max(cen3,dec3,un3)
        men=min(cen3,dec3,un3)
        if men<cen3 and cen3<may:
            print(f"El número es {may}{cen3}{men}")
        elif men<dec3 and dec3<may:
            print(f"El número es {may}{dec3}{men}")
        else:
            print(f"El número es {may}{un3}{men}")
    else:
        print("Número fuera de rango")
else:
    print("Número fuera de opciones")
