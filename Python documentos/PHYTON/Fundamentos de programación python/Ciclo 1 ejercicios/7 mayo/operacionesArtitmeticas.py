a=int(input("Digite un primer número entero: "))
b=int(input("Digite un segundo número entero: "))
if a<0 or b<0:
    print("Número inválido")
else:
    c=int(input("Escriba 1 si quiere sumar, 2 si quiere restar, 3 si quiere multiplicar y 4 si quiere dividir: "))
    if c!=1 and c!=2 and c!=3 and c!=4:
        print("Número inválido")
    elif c==1:
        print("El resultado de su suma es: ",(a+b))
    elif c==2:
        print("El resultado de su resta es: ",(a-b))
    elif c==3:
        print("El resultado de su resta es: ",(a*b))
    elif c==4:
        print("El resultado de su resta es: ",(a/b))
