Algoritmo veterinaria1
	// En una veterinaria se desea saber el promedio de edad de gatos
	// y perros (por separados) que fueron asistidos durante un mes. En total se
	// registraron 30 animales y la veterinaria solo atiende gatos y perros.
	Definir tipo Como Entero
	Para i<-1 Hasta 6 Hacer
		Escribir 'Ingrese tipo de animal '
		Escribir 'Escriba 1 Si es gato'
		Escribir 'Escriba 2 si es perro'
		Escribir 'Escriba 3 si es otro tipo'
		Leer tipo
		Si tipo<1 O tipo>3 Entonces
			Escribir ' Error en la opcion favor escoger una opcion correcta...'
		SiNo
			Si tipo=1 Entonces
				Escribir 'Ingrese la edad del Gato'
				Leer egato
				segato <- segato+egato
				cg <- cg+1
			SiNo
				Si tipo=2 Entonces
					Escribir 'Ingrese la edad del Perro'
					Leer eperro
					seperro <- seperro+eperro
					cp <- cp+1
				SiNo
					Si tipo=3 Entonces
						Escribir 'Ingrese la edad del Animal'
						Leer eotro
						seotro <- seotro+eotro
						co <- co+1
					FinSi
				FinSi
			FinSi
		FinSi
	FinPara
	promg <- segato/cg
	promp <- seperro/cp
	proma <- seotro/co
	Escribir 'Promedio edad de los gatos: ', promg
	Escribir 'Promedio edad de los perros: ', promp
	Escribir 'Promedio edad de los Animales: ', proma
FinAlgoritmo
