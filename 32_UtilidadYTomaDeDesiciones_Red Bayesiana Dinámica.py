#   ENFOQUE:BUSQUEDA EN GRAFOS   #

# LEONARDO DANIEL RAMÍREZ MEDINA #
#        6E1   21310138          #
#        IA - 2DO PARCIAL        #

#Utilidad y Toma de Decisiones - Red Bayesiana Dinámica
#La red bayesiana dinámica (RBD) es un tipo de red bayesiana que modela las relaciones causales entre variables a lo largo del tiempo.


import numpy as np  #Se utiliza para realizar operaciones matemáticas
import networkx as nx   #Se utiliza para crear y manipular grafos
import matplotlib.pyplot as plt #Se utiliza para graficar

# Crear un grafo dirigido acíclico (DAG) para la RBD
G = nx.DiGraph()  # Crear un nuevo grafo dirigido
G.add_nodes_from(["Mañana", "Tarde", "Noche"])  # Agregar nodos al grafo

# Agregar arcos (dependencias) entre las variables
G.add_edge("Mañana", "Tarde")  # Agregar un arco de "Mañana" a "Tarde" ya que un nodo depende del otro
G.add_edge("Tarde", "Noche")  # Agregar un arco de "Tarde" a "Noche"

# Asignar probabilidades condicionales (solo como ejemplo)
prob_mañana = {"Tráfico": 0.7, "Sin tráfico": 0.3}  # Probabilidades para "Mañana"
prob_tarde_dado_mañana = {"Tráfico": 0.8, "Sin tráfico": 0.2}  # Probabilidades para "Tarde" dado "Mañana"
prob_noche_dado_tarde = {"Tráfico": 0.6, "Sin tráfico": 0.4}  # Probabilidades para "Noche" dado "Tarde"

# Visualizar el grafo
pos = nx.spring_layout(G, seed=42)  # Crear una disposición de los nodos
nx.draw(G, pos, with_labels=True, node_size=1000, node_color="skyblue", font_size=10)  # Dibujar el grafo
plt.title("Red Bayesiana Dinámica")  # Agregar un título al gráfico
plt.show()  # Mostrar el gráfico

#Probabilidad de tráfico en la noche dado tráfico en la mañana
prob_mañana_trafico = prob_mañana["Tráfico"]  # Obtener la probabilidad de tráfico en la mañana
prob_tarde_trafico_dado_mañana = prob_tarde_dado_mañana["Tráfico"]  # Obtener la probabilidad de tráfico en la tarde dado tráfico en la mañana
prob_noche_trafico_dado_tarde = prob_noche_dado_tarde["Tráfico"]  # Obtener la probabilidad de tráfico en la noche dado tráfico en la tarde

# Calcula la probabilidad de tráfico en la noche dado tráfico en la mañana
prob_noche_trafico = prob_mañana_trafico * prob_tarde_trafico_dado_mañana * prob_noche_trafico_dado_tarde

# imprime el resultado
print(f"Probabilidad de tráfico en la noche: {prob_noche_trafico:.2f}")