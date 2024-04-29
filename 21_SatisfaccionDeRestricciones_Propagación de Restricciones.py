#   ENFOQUE:BUSQUEDA EN GRAFOS   #

# LEONARDO DANIEL RAMÍREZ MEDINA #
#        6E1   21310138          #
#        IA - 2DO PARCIAL        #

#Satisfacción de Restricciones - Propagación de Restricciones

class Grafo:
    def __init__(self):
        self.vertices = set()  # creamos un conjunto para almacenar los vértices del grafo
        self.aristas = {}      # creamos un diccionario para almacenar las aristas del grafo

    def agregar_vertice(self, v):
        self.vertices.add(v)          # Agrega un vértice al conjunto de vértices
        self.aristas[v] = []          # Inicializa la lista de aristas para ese vértice como vacía

    def agregar_arista(self, u, v):
        self.aristas[u].append(v)     # Agrega una arista entre los vértices u y v

    def propagacion_restricciones(self, camino_actual, nodo_actual):
        # Verifica si el camino actual cumple con las restricciones. No visitar el mismo nodo dos veces
        for nodo in camino_actual:
            if nodo == nodo_actual:
                return False            # Retorna False si el nodo actual ya está en el camino actual

        return True                     # Retorna True si se cumplen las restricciones

    def buscar_camino(self, nodo_actual, nodo_objetivo, camino_actual=[]):
        camino_actual.append(nodo_actual)  # Agrega el nodo actual al camino actual

        if nodo_actual == nodo_objetivo:
            return camino_actual        # Si se llega al nodo objetivo retorna el camino actual

        for vecino in self.aristas[nodo_actual]:
            if self.propagacion_restricciones(camino_actual, vecino):
                # Si se cumplen las restricciones busca el camino desde el vecino
                resultado = self.buscar_camino(vecino, nodo_objetivo, camino_actual)
                if resultado:
                    return resultado   # Si se encuentra un camino válido regresa el resultado

        camino_actual.pop()             # Elimina el último nodo agregado al camino actual
        return None                     # Si no se encuentra ningún camino válido retorna None


#se crea el grafo
grafo1 = Grafo()
grafo1.agregar_vertice("A")
grafo1.agregar_vertice("B")
grafo1.agregar_vertice("C")
grafo1.agregar_arista("A", "B")
grafo1.agregar_arista("B", "C")

# se busca un camino desde A hasta C
camino_encontrado = grafo1.buscar_camino("A", "C")
if camino_encontrado:
    print("Camino encontrado:", " -> ".join(camino_encontrado))
else:
    print("No se encontró un camino válido.")
