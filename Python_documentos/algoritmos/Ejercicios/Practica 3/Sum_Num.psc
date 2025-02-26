Proceso Sum_Num
	Escribir "Ingrese un Numero (0 para calcular)";
	Definir a,tot Como Entero;
	Leer a;
	tot<-0;
	Mientras a<>0 Hacer
		tot<-tot+a;
		Escribir "Ingrese otro Numero (0 para Calcular)";
		Leer a;
	FinMientras
	Escribir "Total: ",tot;
FinProceso
