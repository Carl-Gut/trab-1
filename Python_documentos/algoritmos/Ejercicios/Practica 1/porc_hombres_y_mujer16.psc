Algoritmo porc_hombres_y_mujer
	Escribir "ingrese el total de hombres: "
	Leer h;
	Escribir "Ingrese el total de Mujeres: "
	Leer m;
	total<-h+m;
	porch<- redon((h*100)/total)
	porcm<- redon((m*100)/total)
	Escribir "El porcentaje de hombres es: ",porch
	Escribir "El porcentaje de mujeres es: ",porcm
FinAlgoritmo
