#   ENFOQUE:BUSQUEDA EN GRAFOS   #

# LEONARDO DANIEL RAMÍREZ MEDINA #
#        6E1   21310138          #
#        IA - 2DO PARCIAL        #

#Busqueda no informada - Busqueda en profundidad

def busqueda_profundidad(grafo, actual, objetivo, visitado=None):
    if visitado is None:
        visitado = set()  # se crea el conjunto "visitado" para registrar los nodos por los que hemos pasado
    print(actual, end=' ')  # mostramios el nodo actual
    visitado.add(actual)  # se marca el nodo actual como visitado

    if actual == objetivo:  # Si encontramos el nodo objetivo, terminamos la búsqueda
        print("\nse encontró el objetivo :)")
        return True

    for vecino in grafo[actual]:  # Exploramos los nodos vecinos del nodo actual
        if vecino not in visitado:  # Si un vecino no ha sido visitado, exploramos desde él 
            if busqueda_profundidad(grafo, vecino, objetivo, visitado):
                return True

    print("\nNo se encontró el objetivo :(")  # Si no se encuentra el objetivo, indicamos que no se encontró
    return False

# Creamos el grafo en el que utilizaremos la busqueda en profundidad
grafo = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': [],
    'F': []
}
inicio = 'A'        #Se establece el nodo de inicio de la busqueda
objetivo = 'F'      #establecemos el objetivo a buscar
busqueda_profundidad(grafo, inicio, objetivo)       #se llama a la función de busqueda
