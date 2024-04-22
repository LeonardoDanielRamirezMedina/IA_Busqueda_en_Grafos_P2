#   ENFOQUE:BUSQUEDA EN GRAFOS   #

# LEONARDO DANIEL RAMÍREZ MEDINA #
#        6E1   21310138          #
#        IA - 2DO PARCIAL        #

#Busqueda no informada - Busqueda en anchura de costo uniforme

import heapq

def busq_anchura_costoUni(grafo, inicio, objetivo):
    cola_prioridad = [(0, inicio)]  # Se crea una cola de prioridad para la búsqueda en anchura de costo uniforme
    visitado = set()  # Creamos un conjunto en el que registraremos los nodos visitados

    while cola_prioridad:
        costo, actual = heapq.heappop(cola_prioridad)  # Sacamos el nodo con el menor costo de la cola de prioridad
        print(actual, end=' ')  # se muestra el nodo actual

        if actual == objetivo:  # Si encontramos el nodo que buscamos termina la busqueda
            print("\nse encontró el objetivo :)")
            return True

        visitado.add(actual)  # Marcamos el nodo actual como visitado

        for vecino, costo_vecino in grafo[actual]:  # Exploramos los nodos vecinos del nodo actual
            if vecino not in visitado:  # Si un vecino no ha sido visitado se agrega a la cola de prioridad
                heapq.heappush(cola_prioridad, (costo + costo_vecino, vecino))

    print("\nNo se encontró el objetivo :(")  # Si la cola de prioridad se vacía sin encontrar el objetivo, indicamos que no se encontró
    return False

# Creamos el grafo y sus elementos en el cual utilizaremos la busqueda en anchura de costo uniforme
grafo = {
    'A': [('B', 1), ('C', 2)],
    'B': [('D', 3), ('E', 4)],
    'C': [('F', 5)],
    'D': [],
    'E': [],
    'F': []
}
inicio = 'A'        #Especificamos el inicio
objetivo = 'F'         #Especificamos el nodo buscado
busq_anchura_costoUni(grafo, inicio, objetivo)      #llamamos a la funcion de busqueda