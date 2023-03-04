import random

class Grafo:
	def __init__(self):
		self.grafo_diccionario = {}

	def agregar_nodo(self, nodo):
		self.grafo_diccionario[nodo] = []

	def agregar_conexion(self, nodo1, nodo2):
		self.grafo_diccionario[nodo1].append(nodo2)

	def get_nodo(self, pos):
		con = 1
		for i in self.grafo_diccionario:	
			if con == pos:
				return i
			con += 1

class Nodo:
	def __init__(self, valor, posicion = 0, ant = None):
		self.valor = valor
		self.posicion = posicion
		self.ant = ant

letras = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
pancakes = []
grafo = Grafo()

def crear_grafo():
	posiciones = 2 
	nodo = Nodo(pancakes)
	grafo.agregar_nodo(nodo)
	index = 2
	meta = False
	while not meta:
		for i in range(len(pancakes)-1):
			if posiciones != nodo.posicion:	
				nodo_temp = Nodo(nodo.valor[0:len(pancakes)-posiciones] + nodo.valor[len(pancakes)-posiciones:len(pancakes)][::-1], posiciones, nodo)		
				grafo.agregar_nodo(nodo_temp)
				grafo.agregar_conexion(nodo, nodo_temp)
				if nodo_temp.valor == letras[0:len(pancakes)]:
					meta = True
					break;
			posiciones += 1			
		nodo = grafo.get_nodo(index)
		index += 1
		posiciones = 2

def busquedaAmplitud(nodo):
	cola = []	
	cola.append(nodo)
	while len(cola) > 0:
		nodo = cola.pop(0)
		for i in grafo.grafo_diccionario[nodo]:
			cola.append(i)
	return buscarCamino(nodo)

def buscarCamino(nodo):
	posiciones = []
	while nodo.ant != None:
		posiciones.append(nodo.posicion)
		nodo = nodo.ant
	return posiciones[::-1]

def dibujarPancakes():	
	for i in pancakes:
		indice = letras.index(i)		
		print(" " * (len(pancakes) - indice) + "_" * ((indice + 1) * 2))

def voltearPancakes(posicion):
	pancakes[len(pancakes)-posicion:len(pancakes)] = pancakes[len(pancakes)-posicion:len(pancakes)][::-1]

def juego(noPancakes):
	global pancakes
	pancakes = letras[0:noPancakes]
	random.shuffle(pancakes)
	if pancakes != letras[0:len(pancakes)]:
		crear_grafo()
		posiciones = busquedaAmplitud(grafo.get_nodo(1))
		print("Posición inicial: ")
		dibujarPancakes()
		print("----------------------") 
		for i in posiciones:			
			voltearPancakes(i)
			print(f"posicion : {i}")
			dibujarPancakes()
			print("----------------------")
	else:
		dibujarPancakes()

juego(6)
