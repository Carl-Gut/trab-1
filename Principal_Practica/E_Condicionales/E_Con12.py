print('Programa para eleccion de Pizza!!')
elecc=int(input('Escriba 1 pizza vegetariana o 2 pizza no vegetariana: '))
if elecc >= 3 and elecc <= 0:
    print('Error escriba 1 o 2')
    elif elecc == 1:
    elecc2=int(input('Escriba 1 pimenton o 2 tofu : '))
    if elecc2 >= 3 or elecc <= 0:
        print('Error escriba 1 o 2')
    elif elecc2 == 1:
        print('Escogio Pizza Veg con pimenton, mozzarela y tomate!!!')
    else:
        print('Escogio Pizza Veg con tofu, mozzarela y tomate!!!')  
else:
    elecc3=int(input('Escriba 1 peperonni , 2 jamon o 3 salmon : '))
    if elecc3 >= 4 or elecc <= 0:
        print('Error escriba 1 ,2, 3')
    elif elecc3 == 1:
        print('Escogio Pizza no Veg con peperonni, mozzarela y tomate!!!')
    elif elecc3 == 2:
        print('Escogio Pizza no Veg con jamon, mozzarela y tomate!!!')    
        
    else:
        print('Escogio Pizza no Veg con salmon, mozzarela y tomate!!!')