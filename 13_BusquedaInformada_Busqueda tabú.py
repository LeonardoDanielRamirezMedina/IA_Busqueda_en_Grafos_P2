#   ENFOQUE:BUSQUEDA EN GRAFOS   #

# LEONARDO DANIEL RAMÍREZ MEDINA #
#        6E1   21310138          #
#        IA - 2DO PARCIAL        #

#Busqueda informada - Búsqueda tabú

# Definición del grafo 
grafo = {           #se definen los nodos con sus repextivos aristas y pesos
    'a': [('p', 4), ('j', 15), ('b', 1)],  # Nodo 'a' tiene aristas a 'p', 'j' y 'b' con los respectivos pesos
    'b': [('a', 1), ('d', 2), ('e', 2), ('c', 3)],  
    'j': [('a', 15)],  
    'p': [('a', 4)],  
    'd': [('b', 2), ('g', 3)],  
    'e': [('b', 2), ('g', 4), ('f', 5), ('c', 2)], 
    'c': [('b', 3), ('e', 2), ('f', 5), ('i', 20)], 
    'g': [('d', 3), ('e', 4), ('f', 10), ('h', 1)],  
    'f': [('g', 10), ('e', 5), ('c', 5)],  
    'i': [('c', 20)],  
    'h': [('g', 1)]  
}

# Función de búsqueda tabú
def busqueda_tabu(grafo, origen, destino):
    visitados = []  #  lista donde los nodos visitados
    cola = []  # cola para rbuscar en anchura
    cola.append(origen)  # Agrega el nodo de origen a la cola de búsqueda
    
    while cola:  # Mientras haya nodos en la cola se hace lo siguiente:
        actual = cola.pop(0)  # Obtiene el primer nodo de la cola
        if actual not in visitados:  # Verifica si el nodo actual no ha sido visitado
            print(f"Vertice actual -> {actual}")  # Imprime el nodo actual que está siendo visitado
            visitados.append(actual)  # Agrega el nodo actual a la lista de nodos visitados
            for key, _ in grafo[actual]:  # Itera sobre las aristas del nodo actual
                if key not in visitados:  # Verifica si el nodo vecino no ha sido visitado
                    cola.append(key)  # Agrega el nodo vecino a la cola para ser visitado en la próxima iteración

# Ejemplo de uso
origen = input("Ingresa el nodo origen: ")  # se pide ingresar un nodo de origen
print("\nLista de recorrido en anchura:\n")  
busqueda_tabu(grafo, origen, None)  # Llama a la función de búsqueda tabú con el grafo y el nodo de origen como argumentos
