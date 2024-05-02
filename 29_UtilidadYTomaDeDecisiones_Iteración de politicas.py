#   ENFOQUE:BUSQUEDA EN GRAFOS   #

# LEONARDO DANIEL RAMÍREZ MEDINA #
#        6E1   21310138          #
#        IA - 2DO PARCIAL        #

#Utilidad y Toma de Decisiones - iteración de politicas
#En busqueda en grafos la iteración de politicas es un algoritmo que se utiliza para encontrar la política óptima de un proceso de decisión de Markov.
#Un proceso de decisión de Markov es un modelo matemático que describe un sistema en el que se toman decisiones secuenciales en un entorno incierto.

import networkx as nx

#G es un grafo dirigido que representa un proceso de decisión
G = nx.DiGraph()

# Agregar nodos al grafo
G.add_nodes_from([1, 2, 3, 4, 5])

# Agregar aristas 
edges = [(1, 2), (2, 3), (3, 4), (4, 5), (5, 1)]
G.add_edges_from(edges) # Agregar aristas al grafo

# policy es un diccionario que asigna una acción a cada nodo
policy = {1: 'A', 2: 'B', 3: 'C', 4: 'D', 5: 'E'}

# Iteración de políticas
for _ in range(10):
    for node in G.nodes:
        policy[node] = 'Acción_Aleatoria'   #se asigna una acción aleatoria al nodo

# Imprimir la política final
print("Política final:")
for node, action in policy.items(): #itera sobre los elementos del diccionario
    print(f"Nodo {node}: Acción {action}")  #imprimir el nodo y la acción asignada
