"""
Construya un programa de simulación, en su lenguaje favorito, 
para generar el estado en el paso k de una cadena de Markov  
con transiciones estacionarias y número de estados finitos dado 
un estado inicial, muestre los diferentes estados hasta la 
generación del estado en el paso k.
"""
import pprint
import numpy as np
pp = pprint.PrettyPrinter(indent=4)

def markovChain(n):
	print('empieza cadena markov')

	#Estado inicial
	print('#-----------------------------------------#')
	print('Estado inicial')
	I = np.matrix([[1.0, 0.0,0.0,0.0]])
	pp.pprint(I)

	print('#-----------------------------------------#')
	#Probabilidad
	print('Probabilidad transicion')
	T = np.matrix([
		[0.1, 0.2, 0.3, 0.4],
		[0.3, 0.3, 0.3, 0.1],
		[0.4, 0.2, 0.2, 0.2],
		[0.7, 0.1, 0.1, 0.1]
       	])
	pp.pprint(T)
	print('#-----------------------------------------#')


	for i in range(n):
		print('corrida: ', i)
		if i == 0:
			T_new = I * T
		else:
			T_new = T_new * T

		#print(T_new)
	

	print(T_new)

	print('termina cadena markov')


markovChain(n = 10)
