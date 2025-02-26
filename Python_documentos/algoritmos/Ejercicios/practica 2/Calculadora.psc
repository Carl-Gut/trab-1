Proceso Calculadora
	Escribir "Que operacion quieres Realizar escoger una opcion";
	Escribir "Digita 1 para Sumar";
	Escribir "Digita 2 para Restar";
	Escribir "Digita 3 para Multiplicar";
	Escribir "Digita 4 para Dividir";
	Definir opc,a,b Como Entero;
	Definir c,d,res Como Real;
	res<-0;
	Leer opc;
	
	si opc<=4 Entonces
		si opc=1 Entonces
			Escribir "Digitar el 1 numero";
			Leer a;
			Escribir "Digitar el 2 numero";
			Leer b;
			res<-a+b;
		SiNo
			si opc=2 Entonces
				Escribir "Digitar el 1 numero";
				Leer a;
				Escribir "Digitar el 2 numero";
				Leer b;
				res<-a-b;
			SiNo
				si opc=3 Entonces
					Escribir "Digitar el 1 numero";
					Leer a;
					Escribir "Digitar el 2 numero";
					Leer b;
					res<-a*b;
				SiNo
					si opc=4 Entonces
						Escribir "Digitar el 1 numero";
						Leer c;
						Escribir "Digitar el 2 numero";
						Leer d;
						res<-c/d;
					FinSi
				FinSi
			FinSi
		FinSi
	SiNo
		Escribir "Error en el Numero de Operacion Ingresado";
	FinSi
	Escribir "El resultado de la operacion es: ",res;
FinProceso
