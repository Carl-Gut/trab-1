Algoritmo Calculadora
	//Calculadora Suma , Resta, Multiplicacion y Division
	Escribir "Que operacion desea Realizar:";
	Escribir "1: Sumar";
	Escribir "2: Restar";
	Escribir "3: Multiplicar";
	Escribir "4: Dividir";
	Leer a;
	si a=1 Entonces
		Escribir "Digitar el Primer valor";
		Leer b;
		Escribir "Digitar el Segundo valor";
		Leer c;
		d<-b+c;
		Escribir "La Suma de ",b,"+",c,"=", d;
	SiNo
		si a=2 Entonces
			Escribir "Digitar el Primer Valor";
			Leer b;
			Escribir "Digitar el Segundo Valor";
			Leer c;
			d<-b-c;
			Escribir "La Resta de ",b,"-",c,"=", d;
		SiNo
			si a=3 Entonces
				Escribir "Digitar el Primer Valor";
				Leer b;
				Escribir "Digitar el Segundo Valor";
				Leer c;
				d<-b*c;
				Escribir "La Multiplicacion de ",b,"*",c,"=",d;
			SiNo
				si a=4 Entonces
					Escribir "Digitar el Primer Valor";
					Leer b;
					Escribir "Digitar el Segundo Valor";
					Leer c;
					d<-b/c;
					Escribir "La Division de ",b,"/",c,"=",d;
				FinSi
			FinSi
			
		FinSi
	FinSi
	
	
FinAlgoritmo
