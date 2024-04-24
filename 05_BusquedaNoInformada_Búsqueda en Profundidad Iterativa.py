#   ENFOQUE:BUSQUEDA EN GRAFOS   #

# LEONARDO DANIEL RAMÍREZ MEDINA #
#        6E1   21310138          #
#        IA - 2DO PARCIAL        #

#Busqueda no informada - Búsqueda en Profundidad Iterativa

def busq_prof_iterativa(grafo, inicio, objetivo, profMax):
    
    for depth in range(profMax):            # ciclo for para buscar en cada profundidad hasta el límite máximo
        visited = set()          # se crea un conjunto para llevar un registro de nodos visitados
        stack = [(inicio, 0)]    # Pila para realizar la búsqueda en profundidad iterativa

        # entra el bucle principal de búsqueda en profundidad iterativa
        while stack:
           
            nodo_actual, profundidad_actual = stack.pop()  # Extrae el nodo actual y su profundidad actual desde la pila          
            if nodo_actual == objetivo:     # se comprueba si el nodo actual es el nodo objetivo
                
                print(f"Encontrado en profundidad {profundidad_actual}: {nodo_actual}")
                return True     # Si se encuentra el nodo objetivo, imprime su profundidad y el nodo encontrado y devuelve True

           
            if profundidad_actual < depth:            # Comprueba si la profundidad actual es menor que la profundidad actual de búsqueda           
                visited.add(nodo_actual)        # Añade el nodo actual a los nodos visitados
                neighbors = grafo[nodo_actual]                # Obtiene los vecinos del nodo actual
 
                for neighbor in neighbors:                      # Itera sobre los vecinos del nodo actual

                    if neighbor not in visited:                    # Si el vecino no ha sido visitado, lo agrega a la pila con una profundidad incrementada
                        stack.append((neighbor, profundidad_actual + 1))


    print(f"No se encontró un camino de {inicio} a {objetivo} dentro del límite de profundidad.")    # Si no se encuentra un camino dentro del límite de profundidad, imprime un mensaje y devuelve False
    return False

# Ejemplo de uso
if __name__ == "__main__":
    grafo1 = {
        "A": ["B", "C"],
        "B": ["D", "E"],
        "C": ["F"],
        "D": [],
        "E": ["G"],
        "F": [],
        "G": []
    }

    start = "A"
    obj = "G"
    prof_max_busqueda = 4

    busq_prof_iterativa(grafo1, start, obj, prof_max_busqueda)
