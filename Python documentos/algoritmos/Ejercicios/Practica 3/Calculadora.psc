Proceso Calculadora
	Escribir "Programa Calculadora Elija Una Operacion";
	Escribir "1. Sumar";
	Escribir "2. Restar";
	Escribir "3. Multiplicacion";
	Escribir "4. Division";
	Definir a,b,c,tot Como Entero;
	Definir div Como Real;
	Leer a;
	si a =1 Entonces
		Escribir "Digita el Primer Valor";
		Leer b;
		Escribir "Digita el Segundo Valor";
		Leer c;
		tot<-b+c;
		Escribir " El Resultado de la suma es : ",tot;
	SiNo
		si a=2 Entonces
			Escribir "Digita el Primer Valor";
			Leer b;
			Escribir "Digita el Segundo Valor";
			Leer c;
			tot<-b-c;
			Escribir " El Resultado de la suma es : ",tot;
		SiNo
			si a=3 Entonces
				Escribir "Digita el Primer Valor";
				Leer b;
				Escribir "Digita el Segundo Valor";
				Leer c;
				tot<-b*c;
				Escribir " El Resultado de la suma es : ",tot;
			SiNo
				si a=4 Entonces
					Escribir "Digita el Primer Valor";
					Leer b;
					Escribir "Digita el Segundo Valor";
					Leer c;
					div<-b/c;
					Escribir " El Resultado de la suma es : ",div;
				SiNo
					Escribir "Valor Ingresado fuera de las Opciones";
				FinSi
			FinSi
		FinSi
	FinSi
	
FinProceso
