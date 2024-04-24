#   ENFOQUE:BUSQUEDA EN GRAFOS   #

# LEONARDO DANIEL RAMÍREZ MEDINA #
#        6E1   21310138          #
#        IA - 2DO PARCIAL        #

#Busqueda no informada - Búsqueda bidireccional

def busqueda_bidireccional(graph, inicio, objetivo):
    # Se establecen las fronteras iniciales y se crea un conjunto para los nodos explorados
    frontera_inicio = [inicio]
    frontera_objetivo = [objetivo]
    explorados_inicio = set()
    explorados_objetivo = set()

    # Mientras haya nodos en ambas fronteras
    while frontera_inicio and frontera_objetivo:
        # Se extrae y explora un nodo de la frontera inicial
        actual_inicio = frontera_inicio.pop(0)
        explorados_inicio.add(actual_inicio)

        # Se verifica si el nodo actual es el objetivo o ya ha sido explorado desde el otro extremo
        if actual_inicio == objetivo or actual_inicio in explorados_objetivo:
            # Si se encuentra el objetivo o el nodo ha sido explorado desde el otro extremo, se imprime y se retorna
            print(f"Camino encontrado desde el inicio: {actual_inicio}")
            return

        # Se expanden los vecinos del nodo actual y se agregan a la frontera inicial si no han sido explorados
        for vecino in graph[actual_inicio]:
            if vecino not in explorados_inicio:
                frontera_inicio.append(vecino)

        # Se extrae y explora un nodo de la frontera objetivo
        actual_objetivo = frontera_objetivo.pop(0)
        explorados_objetivo.add(actual_objetivo)

        # Se verifica si el nodo actual es el inicio o si ya ha sido explorado desde el otro extremo
        if actual_objetivo == inicio or actual_objetivo in explorados_inicio:
            # Si se encuentra el inicio o el nodo ha sido explorado desde el otro extremo, se imprime y se retorna
            print(f"Camino encontrado desde el objetivo: {actual_objetivo}")
            return

        # Se expanden los vecinos del nodo actual y se agregan a la frontera objetivo si no han sido explorados
        for vecino in graph[actual_objetivo]:
            if vecino not in explorados_objetivo:
                frontera_objetivo.append(vecino)

    # Si no se encuentra un camino entre los nodos, se imprime un mensaje
    print("No se encontró un camino entre los nodos.")
    return

#uso de la busqueda en el grafdo

if __name__ == "__main__":
    mi_grafo = {
        "A": ["B", "C"],
        "B": ["A", "D"],
        "C": ["A", "E"],
        "D": ["B", "F"],
        "E": ["C", "G"],
        "F": ["D"],
        "G": ["E"]
    }

    nodo_inicio = "A"           #se establece cual será el inicio y objetivo de la buisqueda
    nodo_objetivo = "G"

    busqueda_bidireccional(mi_grafo, nodo_inicio, nodo_objetivo)        #Se llama a la funcion de busqueda bidireccional

