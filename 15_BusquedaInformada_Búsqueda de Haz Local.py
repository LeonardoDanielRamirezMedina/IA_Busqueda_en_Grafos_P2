#   ENFOQUE:BUSQUEDA EN GRAFOS   #

# LEONARDO DANIEL RAMÍREZ MEDINA #
#        6E1   21310138          #
#        IA - 2DO PARCIAL        #

#Busqueda informada - Búsqueda de Haz Local

import heapq  # se usa para implementaciones eficientes de colas de prioridad

class Grafo:
    def __init__(self):
        self.grafo = {}  # Inicializa el diccionario que representa el grafo

    def agregar_arista(self, origen, destino, peso):
        if origen not in self.grafo:
            self.grafo[origen] = []  # Si el nodo de origen no está en el grafo, inicializa su lista de aristas salientes
        self.grafo[origen].append((destino, peso))  # Agrega la arista saliente al nodo de origen con su peso

    def haz_local(self, inicio, k):
        visitados = set()  # Inicializa un conjunto para almacenar los nodos visitados durante la búsqueda
        frontera = [(0, inicio)]  # Inicializa la frontera con una lista que contiene la tupla (costo_acumulado, nodo)
        heapq.heapify(frontera)  # Convierte la lista de frontera en una cola de prioridad utilizando heapq

        while frontera:  # Bucle principal: se ejecuta mientras la frontera no esté vacía
            costo_acumulado, nodo_actual = heapq.heappop(frontera)  # Obtiene el nodo con el menor costo acumulado de la frontera
            visitados.add(nodo_actual)  # Agrega el nodo actual a los nodos visitados

            if len(visitados) >= k:  # Verifica si se han visitado suficientes nodos
                break  # Si se han visitado suficientes nodos, termina la búsqueda

            for vecino, peso in self.grafo.get(nodo_actual, []):  # Itera sobre las aristas salientes del nodo actual
                if vecino not in visitados:  # Verifica si el vecino no ha sido visitado
                    heapq.heappush(frontera, (peso, vecino))  # Agrega el vecino a la frontera con su costo como prioridad

        return visitados  # Devuelve el conjunto de nodos visitados hasta el momento

grafo = Grafo()  # Crea una instancia de la clase Grafo
grafo.agregar_arista('A', 'B', 4)  # Agrega una arista del nodo 'A' al nodo 'B' con peso 4

inicio = 'A'  # Define el nodo de inicio para la búsqueda de haz local
k = 3  # Define el número máximo de nodos a visitar
nodos_visitados = grafo.haz_local(inicio, k)  # Realiza la búsqueda de haz local desde el nodo de inicio
print("Nodos visitados en la búsqueda de haz local:")
print(nodos_visitados)  # Imprime los nodos visitados durante la búsqueda de haz local
