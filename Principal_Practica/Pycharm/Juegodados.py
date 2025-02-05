import random

def lanzar():
    PrimerNumero = random.randint(1,6) 
    SegundoNumero = random.randint(1,6)
    print(f"El primer dado es: {PrimerNumero}")
    print(f"El primer dado es: {SegundoNumero}")
    print(f"El resultado es {PrimerNumero + SegundoNumero}")

while (True): 
    Respuesta = input("¿Quiere lanzar otra vez? (si/no): ")
    if Respuesta.lower() == "si": 
        lanzar() 
    else:
        break  