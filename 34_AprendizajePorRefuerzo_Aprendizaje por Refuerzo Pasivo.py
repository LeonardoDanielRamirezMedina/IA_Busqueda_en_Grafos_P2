#   ENFOQUE:BUSQUEDA EN GRAFOS   #

# LEONARDO DANIEL RAMÍREZ MEDINA #
#        6E1   21310138          #
#        IA - 2DO PARCIAL        #
#Aprendizaje Por Refuerzo - Aprendizaje por Refuerzo Pasivo

#el aprendizaje por refuerzo pasivo es un enfoque en el que el agente no toma decisiones, 
#sino que simplemente observa las recompensas que recibe en cada estado y ajusta sus valores de estado en consecuencia.

import networkx as nx
import matplotlib.pyplot as plt

# Crear un grafo para representar el espacio del estado
G = nx.Graph()

# Agregar nodos al grafo
G.add_nodes_from(range(1, 6))

# Agregar arcos al grafo para representar posibles transiciones
G.add_edges_from([(1, 2), (2, 3), (3, 4), (4, 5), (5, 1)])

# Inicializar los valores de los estados
values = {node: 0 for node in G.nodes}

# Definir las recompensas para cada estado
rewards = {1: 0, 2: 0, 3: 0, 4: 0, 5: 1}  # El estado 5 tiene una recompensa de 1

# Parámetro de descuento
gamma = 0.9

# Realizar el aprendizaje por refuerzo pasivo
for _ in range(1000):  
    current_node = 1  # Comenzar en el estado 1
    while current_node != 5:  # Terminar cuando se llegue al estado 5
        next_node = max(G.neighbors(current_node), key=lambda x: values[x])  # Elegir el vecino con el valor más alto
        values[current_node] += 0.1 * (rewards[current_node] + gamma * values[next_node] - values[current_node])  # Actualizar el valor del estado
        current_node = next_node  # Moverse al siguiente estado

# Dibujar el grafo con los valores de los estados como etiquetas de los nodos
pos = nx.circular_layout(G)
labels = {node: f"{node}: {value:.2f}" for node, value in values.items()}
nx.draw(G, pos, labels=labels, with_labels=True, node_color="skyblue", font_size=10, node_size=1000)
plt.show()