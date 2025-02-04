Algoritmo Ruleta20
	X<-Aleatorio(1,36);
	Escribir "El numero aleatorio es: ",X
	si X<=12 Entonces
		Escribir "El numero pertenece a la primera Docena"
	SiNo
		si X>12 y X<=24 Entonces
			Escribir "El numero pertenece a la segunda Docena"
		SiNo
			si X>24 Entonces
				Escribir "El numero pertenece a la Tercera Docena"
			FinSi
		FinSi
	FinSi
	
FinAlgoritmo
