#   ENFOQUE:BUSQUEDA EN GRAFOS   #

# LEONARDO DANIEL RAMÍREZ MEDINA #
#        6E1   21310138          #
#        IA - 2DO PARCIAL        #

#Busqueda informada - Búsqueda AO*

import heapq  # importamos heapq para usar colas de prioridad
import time  # importamos time para medir el tiempo

class Grafo:
    def __init__(self):
        self.grafo = {}  # Inicializa el grafo como un diccionario vacío

    def agregar_arista(self, origen, destino, peso):
        if origen not in self.grafo:
            self.grafo[origen] = []  # Crea una lista vacía si el nodo de origen no está en el grafo
        self.grafo[origen].append((destino, peso))  # Agrega la arista desde origen a destino con el peso dado
        # Para hacer el grafo no dirigido, agrega también la arista inversa
        if destino not in self.grafo:
            self.grafo[destino] = []  # Crea una lista vacía si el nodo de destino no está en el grafo
        self.grafo[destino].append((origen, peso))  # Agrega la arista desde destino a origen con el peso dado

    def ao_estrella(self, inicio, destino, limite_tiempo):
        abiertos = [(0, inicio)]  # Inicializa una cola de prioridad con el costo acumulado y el nodo inicial
        heapq.heapify(abiertos)  # Convierte la lista de abiertos en una cola de prioridad
        cerrados = set()  # Inicializa un conjunto para almacenar los nodos cerrados
        tiempo_inicio = time.time()  # Obtiene el tiempo actual en segundos

        while abiertos:
            if (time.time() - tiempo_inicio) > limite_tiempo:  # Verifica si ha pasado el límite de tiempo
                break  # Si ha pasado el límite, sale del bucle

            costo_acumulado, nodo_actual = heapq.heappop(abiertos)  # Obtiene el nodo con el menor costo acumulado

            if nodo_actual == destino:  # Verifica si el nodo actual es el destino
                return costo_acumulado  # Devuelve el costo acumulado si ha alcanzado el destino

            cerrados.add(nodo_actual)  # Agrega el nodo actual al conjunto de cerrados

            for vecino, peso in self.grafo.get(nodo_actual, []):  # Itera sobre los vecinos del nodo actual
                if vecino not in cerrados:  # Verifica si el vecino no está en los nodos cerrados
                    # Calcula el costo total sumando el costo acumulado y el peso de la arista
                    costo_total = costo_acumulado + peso
                    heapq.heappush(abiertos, (costo_total, vecino))  # Agrega el vecino a la cola de abiertos con su costo total

        return None  # Si no se encuentra una ruta, devuelve None

# Ejemplo de uso
grafo = Grafo()  # Crea una instancia de la clase Grafo
# aristas al grafo con sus pesos correspondientes
grafo.agregar_arista('A', 'B', 4)
grafo.agregar_arista('A', 'J', 15)
grafo.agregar_arista('A', 'C', 1)
grafo.agregar_arista('B', 'C', 2)
grafo.agregar_arista('B', 'D', 5)
grafo.agregar_arista('C', 'E', 3)
grafo.agregar_arista('D', 'J', 10)
grafo.agregar_arista('D', 'E', 4)
grafo.agregar_arista('E', 'J', 8)

inicio = 'A'  # A es nuestro nodo de inicio
destino = 'J'  # J es nuestro objetivo de busqueda
limite_tiempo = 5  # Define el límite de tiempo en segundos
ruta_mas_corta = grafo.ao_estrella(inicio, destino, limite_tiempo)  # Encuentra la ruta más corta usando AO*

if ruta_mas_corta is not None:  # Verifica si se encontró una ruta
    # Imprime la ruta más corta encontrada
    print(f"La ruta más corta desde {inicio} hasta {destino} es de {ruta_mas_corta} unidades.")
else:
    # Imprime un mensaje si no se encontró una ruta dentro del límite de tiempo
    print(f"No se encontró una ruta desde {inicio} hasta {destino} dentro del límite de tiempo.")
