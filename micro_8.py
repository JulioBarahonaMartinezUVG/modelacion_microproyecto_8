"""
Construya un programa de simulación, en su lenguaje favorito, 
para generar el estado en el paso k de una cadena de Markov  
con transiciones estacionarias y número de estados finitos dado 
un estado inicial, muestre los diferentes estados hasta la 
generación del estado en el paso k.
"""
import numpy as np
import random as rm

def markovChain(n):
	print('empieza cadena markov')

	# Estados del informatico
	states = ["Eat","Sleep","Code", "Repeat"]

	# Possible sequences of events
	transitionName = [
		["EE","ES","EC","ER"],
		["SE","SS","SC","SR"],
		["CE","CS","CC","CR"],
		["RE","RS","RC","RR"]
	]

	# Probabilities matrix (transition matrix)
	transitionMatrix = [
		[0.2,0.6,0.2],
		[0.1,0.6,0.3],
		[0.1,0.6,0.3],
		[0.2,0.7,0.1]
	]


	print('termina cadena markov')


markovChain(10)