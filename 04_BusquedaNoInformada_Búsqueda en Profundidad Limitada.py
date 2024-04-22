#   ENFOQUE:BUSQUEDA EN GRAFOS   #

# LEONARDO DANIEL RAMÍREZ MEDINA #
#        6E1   21310138          #
#        IA - 2DO PARCIAL        #

#Busqueda no informada - Busqueda en profundidad limitada

def busqueda_prof_limit(grafo, actual, objetivo, profundidad_max, visitado=None):
    if visitado is None:
        visitado = set()  # por medio de este conjunto se marcan los nodos ya visitados

    print(actual, end=' ')  # mostramos el nodo actual
    visitado.add(actual)  # se marca como visitado el nodo actual

    if actual == objetivo:  # cuando se encuentre el objetivo acaba la busqueda
        print("\nObjetivo encontrado :)")
        return True

    if profundidad_max <= 0:  # Si alcanzamos la profundidad máxima permitida, detenemos la búsqueda en esta rama
        return False

    for vecino in grafo[actual]:  # Exploramos los nodos vecinos del nodo actual
        if vecino not in visitado:  # Si un vecino no ha sido visitado, exploramos desde él recursivamente con una profundidad reducida
            if busqueda_prof_limit(grafo, vecino, objetivo, profundidad_max - 1, visitado):
                return True

    return False  # Si no se encuentra el objetivo dentro de la profundidad máxima, retornamos False

#Se crea el grafo en el que aplicaremos la busqueda en profundidad limitada
grafo = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': [],
    'F': []
}
inicio = 'A'        #nodo de inicio de la busqueda
objetivo = 'F'      #nodo objetivo de la busqueda
profundidad_maxima = 2  # se establece la profundidad máxima permitida para buscar
busqueda_prof_limit(grafo, inicio, objetivo, profundidad_maxima)        #se llama a la función de busqueda
