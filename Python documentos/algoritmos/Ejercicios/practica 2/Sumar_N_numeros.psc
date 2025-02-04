Proceso Sumar_N_numeros
	Escribir "Ingresar un Numero o 0 para terminar";
	Definir n,tot Como Entero;
	tot<-0;
	Leer n;
	Mientras n<>0 Hacer
		tot<-tot+n;
		Escribir "ingrese el siguiente numero 0 para terminar";
		Leer n;
	FinMientras
	escribir "La suma Total de los numeros es: ",tot;
FinProceso
