Algoritmo factorial22
	Escribir "Ingrese el fumero para Fctorizar: "
	Leer N;
	Z<-N
	nfact<-1
	Mientras N<>1 Hacer
		nfact<-nfact+(nfact*(N-1))
		N<-N-1
		Escribir N
	FinMientras
	Escribir "El factorial de ",Z," es: ",nfact
	
FinAlgoritmo
