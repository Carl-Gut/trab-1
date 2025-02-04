Algoritmo par_e_imp20
	//Solicitar al usuario que ingrese un número entero N, luego
	//generar en forma aleatoria N números enteros comprendidos entre 1 y 100
	//y determinar cuántos son pares y cuántos impares.
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
