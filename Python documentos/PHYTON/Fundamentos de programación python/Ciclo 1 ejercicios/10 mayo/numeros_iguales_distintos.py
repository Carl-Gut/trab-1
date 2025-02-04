#Escribir 3 números y decir sí son iguales o diferentes, o 2 iguales#
n1=int(input("Escriba primer número: "))
n2=int(input("Escriba segundo número: "))
n3=int(input("Escriba tercer número: "))
if n1==n2 and n2==n3:
    print("Los números son iguales")
elif n1==n2 and n2!=n3:
    print("El primer y segundo número son iguales")
elif n2==n3 and n2!=n1:
    print("El segundo y tercer número son iguales")
elif n1==n3 and n1!=n2:
    print("El primer y tercer número son iguales")
else:
    print("Los números son diferentes")
