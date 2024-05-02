#   ENFOQUE:BUSQUEDA EN GRAFOS   #

# LEONARDO DANIEL RAMÍREZ MEDINA #
#        6E1   21310138          #
#        IA - 2DO PARCIAL        #
#Aprendizaje Por Refuerzo - Exploración vs. Explotación

#La exploracion serefiere a la busquerda de nuesvas soluciones.Es la elección de una opción desconocida para aprender más sobre ella.


class Grafo:
    def __init__(self): # Constructor de la clase
        self.vertices = {}  # Diccionario para almacenar los vértices y sus sucesores con pesos
    
    def agregar_vertice(self, v):   # Método para agregar un vértice al grafo
        self.vertices[v] = []  # Inicializamos la lista de sucesores para el vértice v
    
    def agregar_arista(self, u, v, peso):   # Método para agregar una arista con peso entre dos vértices
        self.vertices[u].append((v, peso))  # Agregamos una arista con su peso
    
    def dfs_exploracion(self, u, visitados):    # Método para realizar una búsqueda en profundidad (DFS) desde un vértice
        visitados.add(u)  # Marcamos el vértice como visitado
        print(u, end=" ")  # Imprimimos el vértice visitado
        
        for sucesor, peso in self.vertices[u]:  # Iteramos sobre los sucesores del vértice
            if sucesor not in visitados:    
                self.dfs_exploracion(sucesor, visitados)  # Llamada recursiva para los sucesores no visitados


grafo = Grafo()     # Creamos un grafo con pesos
grafo.agregar_vertice(1)    # Agregamos los vértices al grafo
grafo.agregar_vertice(2)
grafo.agregar_vertice(3)
grafo.agregar_vertice(4)

grafo.agregar_arista(1, 2, 30)  # Agregamos las aristas con pesos
grafo.agregar_arista(1, 3, 20)
grafo.agregar_arista(2, 4, 20)
grafo.agregar_arista(3, 4, 50)


visitados = set()   # Creamos un conjunto para almacenar los vértices visitados
print("Recorrido DFS desde el vértice 1 (exploración):")    
grafo.dfs_exploracion(1, visitados) # Realizamos un recorrido DFS desde el vértice 1
