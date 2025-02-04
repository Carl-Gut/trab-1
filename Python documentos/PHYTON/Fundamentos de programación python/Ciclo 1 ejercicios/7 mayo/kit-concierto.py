bol=int(input("Por favor escriba los 4 números de su boleta: "))
if bol<0:
    print("Error")
else:
    mil=bol//1000
    mil1=bol%1000
    cen=mil1//100
    cen1=mil1%100
    dec=cen1//10
    primernum=mil%2
    segundonum=dec%2
    if primernum==0 and segundonum!=0:
        print("Eres ganador de un Kit Carnavalero gratis")
    else:
        pago=int(input("No ganaste el Kit Carnavalero, pero puedes comprarlo. \n Sí deseas comprarlo escribe 1, de lo contrario escribe 2: "))
        if pago==2:
            print("Gracias. Será en otra oportunidad")
        elif pago==1:
            edad=int(input("El Kit Carnavalero cuesta $100.000, pero tenemos descuentos.\n Escribe tu edad para saber si aplicas: "))
            if edad<=25:
                print("Tu kit tiene un descuento del 15%, debes pagar $85.000")
            elif edad>=60:
                print("Tu kit tiene un descuento del 30%, debes pagar $70.000")
            else:
                print("No hay descuento para ti, pero puedes obtener el KIt por $100.000")
