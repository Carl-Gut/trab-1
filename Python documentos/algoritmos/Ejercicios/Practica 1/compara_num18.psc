Algoritmo compara_num
	Escribir "ingrese el valor del Numero 1: "
	Leer num1;
	Escribir "ingrese el valor del Numero 2: "
	Leer num2;
	Escribir "ingrese el valor del Numero 3: "
	Leer num3;
	si num1>num2 y num2>num3 Entonces
		Escribir "El mayor es: ",num1
	FinSi
	si num1<num2 y num2>num3 Entonces
		Escribir "El mayor es: ",num2
	FinSi
	si num1<num2 y num2<num3 Entonces
		Escribir "El mayor es: ",num3
	FinSi
FinAlgoritmo
