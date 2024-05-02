#   ENFOQUE:BUSQUEDA EN GRAFOS   #

# LEONARDO DANIEL RAMÍREZ MEDINA #
#        6E1   21310138          #
#        IA - 2DO PARCIAL        #
#Aprendizaje Por Refuerzo - Aprendizaje por Refuerzo Activo

#el aprendizaje por refuerzo activo es un enfoque en el que el agente toma decisiones para maximizar las recompensas que recibe en cada estado.

import networkx as nx   #se usa para trabajar con grafos
import matplotlib.pyplot as plt  #se usa para graficar
from queue import Queue #se usa para implementar una cola

# creamos un grafo para representar el espacio del estado
G = nx.Graph()
G.add_edges_from([(0, 1), (0, 2), (1, 3), (2, 3)])  #definiendo las conexiones entre los nodos

# definimos el estado inicial y objetivo
estado_inicial = 0
estado_objetivo = 3

# Algoritmo de búsqueda en anchura (BFS)
def bfs(grafo, inicio, objetivo):   #la fincion recibe el grafo, el estado inicial y el estado objetivo
    visitados = set()   #creamos un conjunto vacio para almacenar los nodos visitados
    cola = Queue()  #creamos una cola para almacenar los nodos que se van a visitar
    cola.put(inicio)    #agregamos el estado inicial a la cola

    while not cola.empty(): #mientras la cola no este vacia
        actual = cola.get() #obtenemos el primer elemento de la cola
        if actual == objetivo:  #si el nodo actual es igual al nodo objetivo
            return True #retornamos True
        visitados.add(actual)
        for vecino in grafo.neighbors(actual):  
            if vecino not in visitados: 
                cola.put(vecino)    #agregamos el vecino a la cola
    return False    #si no se encuentra el nodo objetivo retornamos False

# Ejecutar la búsqueda
if bfs(G, estado_inicial, estado_objetivo):     
    print("Se encontró un camino desde el estado inicial al objetivo.") #si se encuentra un camino imprimimos un mensaje
else:
    print("No se encontró un camino desde el estado inicial al objetivo.")  #si no se encuentra un camino imprimimos un mensaje

# Visualizar el grafo
nx.draw(G, with_labels=True, node_color='lightblue', font_weight='bold')    #dibujamos el grafo
plt.show()  #mostramos el grafo
