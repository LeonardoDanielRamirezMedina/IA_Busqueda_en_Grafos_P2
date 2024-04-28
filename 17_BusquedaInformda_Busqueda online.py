#   ENFOQUE:BUSQUEDA EN GRAFOS   #

# LEONARDO DANIEL RAMÍREZ MEDINA #
#        6E1   21310138          #
#        IA - 2DO PARCIAL        #

#Busqueda informada - Búsqueda online

import random  # importamos random para utilizar numeros aleatorios

class Grafo:
    def __init__(self):
        self.grafo = {}  # se inicializa el grafo

    def agregar_arista(self, origen, destino, peso):
        if origen not in self.grafo:
            self.grafo[origen] = []  # si el nodo de origen no se encuentra en el grafo entonces se crea una lista para almacenar aristas
        self.grafo[origen].append((destino, peso))  # Agrega la arista al nodo de origen en el grafo

    def busqueda_online(self, inicio, k):
        visitados = set()  # Conjunto de nodos visitados
        nodos_por_visitar = [inicio]  # Lista de nodos que deben ser visitados

        while nodos_por_visitar and len(visitados) < k:  # Mientras haya nodos por visitar y no se haya alcanzado el límite k
            nodo_actual = nodos_por_visitar.pop(random.randint(0, len(nodos_por_visitar)-1))  # Selecciona un nodo aleatorio de los nodos por visitar
            visitados.add(nodo_actual)  # Agrega el nodo actual a los nodos visitados

            for vecino, _ in self.grafo.get(nodo_actual, []):  # Itera sobre los vecinos del nodo actual
                if vecino not in visitados:  # Verifica si el vecino no ha sido visitado
                    nodos_por_visitar.append(vecino)  # Agrega el vecino a la lista de nodos por visitar

        return visitados  # Devuelve los nodos visitados hasta el momento


grafo = Grafo()
grafo.agregar_arista('A', 'B', 4)
grafo.agregar_arista('A', 'C', 2)
grafo.agregar_arista('B', 'D', 5)
grafo.agregar_arista('C', 'E', 3)
grafo.agregar_arista('D', 'F', 6)
grafo.agregar_arista('E', 'F', 1)

inicio = 'A'  # se establece cual es el ndodo de inicio
k = 3  # Número máximo de nodos a visitar

nodos_visitados = grafo.busqueda_online(inicio, k)
print("Nodos visitados en la búsqueda en línea:")
print(nodos_visitados)
