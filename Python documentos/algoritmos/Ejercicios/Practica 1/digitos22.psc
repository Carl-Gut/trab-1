Algoritmo digitos22
	Escribir "Escriba un numero de hasta cuatro cifras: "
	Leer X;
	si X<10 Entonces
		d1<-0
		d2<-0
		d3<-0
		d4<-X
		Escribir "los numeros son d1: ",d1,"d2: ",d2,"d3: ",d3,"d4: ",d4
	SiNo
		si X>=10 y X<=99 Entonces
			d1=0
			d2=0
			tex<-ConvertirATexto(X);
			d5<-SubCadena((tex),1,1);
			d6<-SubCadena((tex),2,2);
			Escribir "los numeros son d1: ",d1," d2: ",d2," d3: ",d5," d4: ",d6
			x1<-ConvertirANumero(d5);
			x2<-ConvertirANumero(d6);
			sum<-x1+x2;
			Escribir "la suma de los digitos es: ",sum
		SiNo
			si X>=100 y X<=999 Entonces
				d1=0
				tex<-ConvertirATexto(X);
				d5<-SubCadena((tex),1,1);
				d6<-SubCadena((tex),2,2);
				d7<-SubCadena((tex),3,3);
				Escribir "los numeros son d1: ",d1," d2: ",d5," d3: ",d6," d4: ",d7
				x1<-ConvertirANumero(d5);
				x2<-ConvertirANumero(d6);
				x3<-ConvertirANumero(d7);
				sum<-x1+x2+x3;
				Escribir "la suma de los digitos es: ",sum
			SiNo
				si X>=1000 y X<=9999 Entonces
					tex<-ConvertirATexto(X);
					d5<-SubCadena((tex),1,1);
					d6<-SubCadena((tex),2,2);
					d7<-SubCadena((tex),3,3);
					d8<-SubCadena((tex),4,4);
					Escribir "los numeros son d1: ",d5," d2: ",d6," d3: ",d7," d4: ",d8
					x1<-ConvertirANumero(d5);
					x2<-ConvertirANumero(d6);
					x3<-ConvertirANumero(d7);
					x4<-ConvertirANumero(d8);
					sum<-x1+x2+x3+x4;
					Escribir "la suma de los digitos es: ",sum
				FinSi
				
			FinSi
			
		FinSi
	FinSi
	
	
	
FinAlgoritmo
