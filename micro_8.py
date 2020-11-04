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

def multMatrices(X,Y):
	result = [[0,0,0,0]]	
	for i in range(len(X)):
	   for j in range(len(Y[0])):
	       for k in range(len(Y)):
	           result[i][j] += X[i][k] * Y[k][j]

	print(result)

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
			
		print(T_new)

	print('termina cadena markov')
	

	return(T_new)


ej1 = markovChain(n = 10)
print('Resultado final: \\n',ej1)


"""
Utilice el algoritmo de Hastings-Metrópolis para generar los 
valores de una variable normal estándar, sea q(x,y) definido 
como y=x+e donde los valores de e se generan de una variable 
aleatoria G con g función de densidad de probabilidad simétrica 
en 0. Además, q(x,y)=g(e).Realice el histograma con los 10000 valores resultantes.
"""

import numpy as np
import math
from numpy import linalg as la
import matplotlib.pyplot as plt
import matplotlib.mlab as mlab
import time

mu,sig,N = 0,1,1000000
pts = []

def q(x):
    return (1/(math.sqrt(2*math.pi*sig**2)))*(math.e**(-((x-mu)**2)/(2*sig**2)))

def metropolis(N):
    r = np.zeros(1)
    p = q(r[0])
    pts = []
    
    for i in range(N):
        rn = r + np.random.uniform(-1,1)
        pn = q(rn[0])
        if pn >= p:
            p = pn
            r = rn
        else:
            u = np.random.rand()
            if u < pn/p:
                p = pn
                r = rn
        pts.append(r)
    
    pts = np.array(pts)
    return pts
    
def hist_plot(array):
    fig = plt.figure()
    ax = fig.add_subplot(1,1,1,)
    ax.hist(array, bins=1000)    
    plt.title('')
    plt.xlabel('')
    plt.ylabel('')
    plt.savefig('ej2.png')

x = metropolis(10000)

hist_plot(x)    