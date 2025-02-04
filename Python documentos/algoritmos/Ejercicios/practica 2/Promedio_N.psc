Proceso Promedio_N
	Escribir "Ingresar la cantidad de Datos";
	Definir N,acum,i,dato Como Entero;
	Definir prom Como Real;
	Leer N;
	acum<-0;
	para i<-1 Hasta N Hacer
		Escribir "Ingresar el dato ",i," :";
		Leer dato;
		acum<-acum+dato;
	FinPara
	prom<-acum/N;
	Escribir "El Promedio es : ",prom;
FinProceso
