Proceso Promedio
	Escribir "Ingresar la cantidad de Datos";
	Definir N,acum,i,dato Como Entero; 
	Definir prom Como Real;
	Leer N;
	acum<-0;
	para i<-1 Hasta N Hacer
		Escribir "Ingresar el valor de ",i,":";
		Leer dato;
		acum<- acum+dato;
	FinPara
	prom<-acum/N;
	Escribir "El promedio es: ",prom;
FinProceso
