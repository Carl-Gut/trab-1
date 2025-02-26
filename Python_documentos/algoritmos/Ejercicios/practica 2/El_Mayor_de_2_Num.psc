Proceso El_Mayor_de_2_Num
	Escribir "Ingresar Los Numeros a Comparar";
	Definir a,b Como Entero;
	Escribir "Primer Numero";
	Leer a;
	Escribir "Segundo Numero";
	Leer b;
	si a>b Entonces
		Escribir "El numero ",a," Es mayor que ",b;
	SiNo
		si b>a Entonces
			Escribir "El numero ",b," Es mayor que ",a;
		FinSi
	FinSi
	
FinProceso
