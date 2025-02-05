barra_N=3.49
b_vieja=barra_N-(barra_N*0.6)
barr_vend=int(input('ingresar numero de barras vendidas: '))
cost_b=b_vieja*barr_vend
print('costo de barra de pan: ', barra_N)
print('costo de barra no del dia: ', round(b_vieja,2))
print('costo total de venta: ', round(cost_b,2))