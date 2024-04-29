#   ENFOQUE:BUSQUEDA EN GRAFOS   #

# LEONARDO DANIEL RAMÍREZ MEDINA #
#        6E1   21310138          #
#        IA - 2DO PARCIAL        #

#Satisfacción de Restricciones - Búsqueda de Vuelta Atrás

class Graph:
    def __init__(self, edges, num_vertices):
        self.adj_list = [[] for _ in range(num_vertices)]  # Inicializa una lista de adyacencia vacía para cada vértice
        for edge in edges:
            self.adj_list[edge[0]].append(edge[1])            # Añade las aristas bidireccionales al grafo
            self.adj_list[edge[1]].append(edge[0])            # Añade las aristas bidireccionales al grafo

    def dfs(self, vertex, discovered):
        discovered[vertex] = True  # Marca el vértice como descubierto
        print(f"Explorando nodo {vertex}")

        # Recorre todos los vecinos del vértice actual
        for neighbor in self.adj_list[vertex]:
            if not discovered[neighbor]:  # Si el vecino no ha sido descubierto
                self.dfs(neighbor, discovered)  # Realiza una búsqueda en profundidad desde ese vecino

if __name__ == "__main__":
    # Laberinto con nodos numerados del 0 al 9
    edges = [(0, 1), (0, 2), (1, 3), (1, 4), (2, 5), (2, 6), (3, 7), (4, 8), (5, 9)]

    num_vertices = 10  # Número total de nodos en el grafo
    graph = Graph(edges, num_vertices)  # Crea el grafo a partir de las aristas y el número de vértices
    discovered = [False] * num_vertices  # Lista para rastrear los nodos descubiertos durante el DFS

    start_node = 0  # Comenzamos en el nodo 0
    print("Recorrido en profundidad (DFS):")
    graph.dfs(start_node, discovered)  # Realiza un recorrido en profundidad desde el nodo inicial
