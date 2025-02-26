Algoritmo Volum_cilindr14
	Escribir "Ingrese el valor del radio: "
	Leer r;
	Mientras r<0 Hacer
		Escribir "Valor Errado favor ingrese el valor nuevamente:  "
		Leer r;
	FinMientras
	Escribir "Ingrese el valor de la altura: "
	Leer h;
	Mientras  h<0 Hacer
		Escribir "Valor Errado favor ingrese el valor nuevamente:  "
		Leer h;
	FinMientras
	vol<-trunc((PI)*(r^2)*h);
	Escribir "El volumen del cilindro es: ",vol;
	
FinAlgoritmo
