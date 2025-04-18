from decorators import delta_time


@delta_time("GRUPO GN")
def Carmichael(inicio,fin):
	return

if __name__ == "__main__":
	#INGRESO DATOS
	'''
	op 1 con tope: ej 1000 / inicio= 1 fin =1000
	op 2 con cifras: ej 6 / inicio 100000 fin= 999999
	'''
	tope = input(int("Ingrese tope: "))

	print(Carmichael(1,tope))