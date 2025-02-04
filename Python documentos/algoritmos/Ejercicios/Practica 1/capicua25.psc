Algoritmo capicua25
	x<-Aleatorio(10000,99999);
	Escribir x;
	t<-ConvertirATexto(x);
	t1<-SubCadena(t,1,1);
	t2<-SubCadena(t,2,2);
	t4<-SubCadena(t,4,4);
	t5<-SubCadena(t,5,5);
	n1<-ConvertirANumero(t1);
	n2<-ConvertirANumero(t2);
	n4<-ConvertirANumero(t4);
	n5<-ConvertirANumero(t5);
	si n1=n5 y n2=n4 Entonces
		Escribir "SORPRESA EL NUMERO ES CAPICUA!!!"
	SiNo
		Escribir "No lo es Continua..."
	FinSi
	
FinAlgoritmo
