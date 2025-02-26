Proceso Tiempo_Transcurrido
	Escribir "Escriba por favor la hora inicial y la hora Final";
	Escribir "Hora Inicial: (Hh,Mm)";
	Definir  H1,H2,M1,M2,dh,dm como entero;
	Leer H1;
	Leer M1;
	Escribir "Hora Final: (Hh,Mm)";
	Leer H2;
	Leer M2;
    dh<-H2-H1;
	dm<-M2-M1;
	si dh<0 Entonces
		dh<-(-1*dh);
	SiNo
		dh<-dh;
	FinSi
	si dm<0 Entonces
		dm<-(-1*dm);
	SiNo
		dm<-dm;
	FinSi
	Escribir "El tiempo transcurrido es: ",dh," Horas con ",dm," Minutos";
FinProceso
