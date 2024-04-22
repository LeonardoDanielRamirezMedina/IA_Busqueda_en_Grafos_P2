#   ENFOQUE:BUSQUEDA EN GRAFOS   #

# LEONARDO DANIEL RAMÍREZ MEDINA #
#        6E1   21310138          #
#        IA- 2DO PARCIAL         #

#Busqueda no informada - Busqueda en anchura

from collections import deque

def busqueda_anchura(grafo, inicio, objetivo):
    cola = deque()  # se crea una cola o fila para buscar en anchura
    revisado = set()  # se crea el conjunto "revisado" para registrar los nodos que ya visitamos

    cola.append(inicio)  # Empezamos desde el nodo inicial tomando como parametro la variable inicio
    revisado.add(inicio)  # Marcamos el nodo inicial como visitado

    while cola:
        actual = cola.popleft()  # Sacamos el primer elemento de la cola
        print(actual, end=' ')  # Imprimimos el nodo actual

        if actual == objetivo:  # si nuestro objetivo coincide mcon el nodo actual termina la busqueda
            print("\nSe encontró el objetivo :)")
            return True

        for vecino in grafo[actual]:  # Exploramos los nodos vecinos del nodo actual
            if vecino not in revisado:  # Si un vecino no ha sido visitado, lo agregamos a la cola y lo marcamos como visitado
                cola.append(vecino)
                revisado.add(vecino)

    print("\nNo se encontró el objetivo :(")  # Si la cola se vacía sin encontrar el objetivo, indicamos que no se encontró
    return False

# se declara el grafo con sus elementos que utilizaremos para la busqueda
grafo = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': [],
    'F': []
}
inicio = 'A'    #Se establece el inicio del grafo
objetivo = 'E'  #Se indica el nodo que buscamos dentro del grafo
busqueda_anchura(grafo, inicio, objetivo)       #se llama a la función para la busqueda en anchura
