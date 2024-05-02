#   ENFOQUE:BUSQUEDA EN GRAFOS   #

# LEONARDO DANIEL RAMÍREZ MEDINA #
#        6E1   21310138          #
#        IA - 2DO PARCIAL        #
#Aprendizaje Por Refuerzo - Exploración vs. Explotación

#La explotacion es la elección de la mejor opción conocida

class Grafo:    # Clase para representar un grafo con pesos
    def __init__(self):
        self.vertices = {}  # Diccionario para almacenar los vértices y sus sucesores con pesos
    
    def agregar_vertice(self, v):   # Método para agregar un vértice al grafo
        self.vertices[v] = []  # Inicializamos la lista de sucesores para el vértice v
    
    def agregar_arista(self, u, v, peso):   # Método para agregar una arista con peso entre dos vértices
        self.vertices[u].append((v, peso))  # Agregamos una arista con su peso
    
    def buscar_camino_explotacion(self, u, v, costo_max):   # Método para buscar un camino entre dos vértices con un costo máximo
        visitados = set()   # Creamos un conjunto para almacenar los vértices visitados
        return self._dfs_explotacion(u, v, costo_max, visitados)    # Llamada al método auxiliar DFS
    
    def _dfs_explotacion(self, u, v, costo_max, visitados):   # Método auxiliar para realizar una búsqueda en profundidad (DFS) desde un vértice
        visitados.add(u)    # Marcamos el vértice como visitado
        
        if u == v:
            return [(u, 0)]  # Llegamos al destino con costo 0
        
        for sucesor, peso in self.vertices[u]:  #en las siguientes líneas se realiza la busqueda de la mejor opción conocida
            if sucesor not in visitados and peso <= costo_max:
                camino = self._dfs_explotacion(sucesor, v, costo_max - peso, visitados)
                if camino:
                    return [(u, peso)] + camino # Retornamos el camino encontrado
        
        return None


grafo = Grafo() #creamos un grafo para la busqueda de la mejor opción conocida
grafo.agregar_vertice(1)    # Agregamos los vértices al grafo
grafo.agregar_vertice(2)
grafo.agregar_vertice(3)
grafo.agregar_vertice(4)

grafo.agregar_arista(1, 2, 30)  # Agregamos las aristas con pesos
grafo.agregar_arista(1, 3, 20)
grafo.agregar_arista(2, 4, 20)
grafo.agregar_arista(3, 4, 50)

# Buscar un camino desde el vértice 1 al 4 con costo máximo 60
camino_explotacion = grafo.buscar_camino_explotacion(1, 4, 60)  # Buscamos un camino con costo máximo 60
if camino_explotacion:  
    print("Camino encontrado (vértice, costo):", camino_explotacion)    # Imprimimos el camino encontrado
else:
    print("No se encontró un camino válido.")   # Mensaje si no se encontró un camino válido
