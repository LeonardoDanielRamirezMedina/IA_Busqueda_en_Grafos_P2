#   ENFOQUE:BUSQUEDA EN GRAFOS   #

# LEONARDO DANIEL RAMÍREZ MEDINA #
#        6E1   21310138          #
#        IA - 2DO PARCIAL        #

#Busqueda informada - Heurísticas

import heapq  # Importa el módulo heapq para la implementación de la cola de prioridad

def distancia(nodo_actual, nodo_objetivo):
    # Calcula la distancia que hay entre dos nodos en una cuadrícula
    x1, y1 = nodo_actual
    x2, y2 = nodo_objetivo
    return abs(x2 - x1) + abs(y2 - y1)

def a_estrella(inicio, objetivo, grafo):
    # Inicializa la frontera como una lista de tuplas (prioridad, nodo)
    frontera = [(0, inicio)]
    heapq.heapify(frontera)  # Convierte la lista en una cola de prioridad
    came_from = {}  # Almacena el nodo padre de cada nodo en el camino encontrado
    costo_g = {inicio: 0}  # Almacena el costo real desde el nodo inicial hasta cada nodo

    while frontera:
        _, actual = heapq.heappop(frontera)  # Obtiene el nodo con la menor prioridad de la frontera

        if actual == objetivo:  # Si se alcanza el objetivo, reconstruye y devuelve el camino
            camino = reconstruir_camino(came_from, inicio, objetivo)
            return camino

        for vecino in grafo[actual]:  # Para cada vecino del nodo actual
            nuevo_costo_g = costo_g[actual] + 1  # Costo uniforme de moverse a un vecino
            if vecino not in costo_g or nuevo_costo_g < costo_g[vecino]:
                costo_g[vecino] = nuevo_costo_g
                # Calcula la prioridad del vecino sumando el costo actual y la heurística
                prioridad = nuevo_costo_g + distancia(vecino, objetivo)
                heapq.heappush(frontera, (prioridad, vecino))  # Agrega el vecino a la frontera
                came_from[vecino] = actual  # Registra el nodo actual como padre del vecino

    return None

def reconstruir_camino(came_from, inicio, objetivo):
    # Reconstruye el camino desde el objetivo hasta el inicio
    actual = objetivo
    camino = [actual]
    while actual != inicio:
        actual = came_from[actual]
        camino.append(actual)
    camino.reverse()
    return camino

# Creamos el grafo en el que se arealizará la búsqueda
grafo = {  # definimos el grafo como un diccionario donde las claves son nodos y los valores son conjuntos de vecinos
    (0, 0): {(0, 1), (1, 0)},
    (0, 1): {(0, 0), (0, 2)},
    (0, 2): {(0, 1), (1, 2)},
    (1, 0): {(0, 0), (1, 1)},
    (1, 1): {(1, 0), (1, 2)},
    (1, 2): {(0, 2), (1, 1)}
}

inicio = (0, 0)  # Nodo inicial
objetivo = (0, 2)  # Nodo objetivo

camino = a_estrella(inicio, objetivo, grafo)  # Ejecuta el algoritmo A*
print("Camino encontrado:", camino)  # Imprime el camino encontrado