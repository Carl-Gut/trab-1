Algoritmo par_e_imp20
	//Solicitar al usuario que ingrese un n�mero entero N, luego
	//generar en forma aleatoria N n�meros enteros comprendidos entre 1 y 100
	//y determinar cu�ntos son pares y cu�ntos impares.
	Escribir "Escriba un numero entero : "
	Leer n;
	para i<-1 Hasta n Hacer
		x<-Aleatorio(1,100);
		si x mod 2=0 Entonces
			contpar<-contpar+1
			Escribir x;
		SiNo
			contimp<-contimp+1
			Escribir x;
			
		FinSi
	FinPara
	Escribir "Los numeros pares fueron: ",contpar
	Escribir "Los numeros impares fueron: ",contimp
	
FinAlgoritmo
