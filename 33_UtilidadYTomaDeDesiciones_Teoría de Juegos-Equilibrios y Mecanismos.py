#   ENFOQUE:BUSQUEDA EN GRAFOS   #

# LEONARDO DANIEL RAMÍREZ MEDINA #
#        6E1   21310138          #
#        IA - 2DO PARCIAL        #
#Utilidad y Toma de Decisiones - Teoría de Juegos: Equilibrios y Mecanismos
#La teoría de juegos es una rama de las matemáticas que estudia las interacciones estratégicas entre agentes racionales.
#equilibrio y mecanismos se refiere a la teoría de juegos y a los mecanismos de diseño que se utilizan para garantizar que los agentes tomen decisiones óptimas.

import networkx as nx
import matplotlib.pyplot as plt

# Crear un grafo para representar el espacio del juego
G = nx.Graph()

# Agregar nodos al grafo
G.add_nodes_from(range(1, 6))   # Nodos del 1 al 5

# Agregar arcos al grafo para representar posibles movimientos
G.add_edges_from([(1, 2), (2, 3), (3, 4), (4, 5), (5, 1)])      #add_edges_from() agrega arcos al grafo

# Dibujar el grafo
pos = nx.circular_layout(G)   #pos es un diccionario que contiene las posiciones de los nodos
nx.draw(G, pos, with_labels=True, node_color="skyblue", font_size=10, node_size=1000)   #nx.draw() dibuja el grafo
plt.title("Juego de Búsqueda")  #plt.title() agrega un título al gráfico
plt.show()  # muestra el gráfico

# Definir el nodo donde se encuentra el jugador oculto
hidden_player = 3

# El buscador comienza en el nodo 1 y sigue una estrategia de búsqueda en profundidad
current_node = 1    #nodo actual
visited = {current_node}    #conjunto de nodos visitados

while current_node != hidden_player:    #mientras el nodo actual no sea el nodo del jugador oculto
    for neighbor in G.neighbors(current_node):   #en las siguyientes lineas se recorren los nodos vecinos del nodo actual
        if neighbor not in visited: 
            visited.add(neighbor)
            current_node = neighbor
            break

print(f"El jugador oculto fue encontrado en el nodo {current_node}")    #imprime el nodo donde se encuentra el jugador oculto
