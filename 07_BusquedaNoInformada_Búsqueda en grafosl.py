#   ENFOQUE:BUSQUEDA EN GRAFOS   #

# LEONARDO DANIEL RAMÍREZ MEDINA #
#        6E1   21310138          #
#        IA - 2DO PARCIAL        #

#Busqueda no informada - Búsqueda en grafos

class Grafo:
    def __init__(self, adyacencia):
        # Inicia la clase Grafo con el diccionario de adyacencia proporcionado
        self.adyacencia = adyacencia

    def profundidad(self, nodo):
        # Realiza un recorrido en profundidad comenzando desde el nodo dado
        visitados = set()  # Guarda los nodos visitados durante el recorrido
        pila = [nodo]  # Utiliza una pila para mantener el orden de exploración

        while pila:
            actual = pila.pop()  # Extrae el último nodo de la pila

            if actual not in visitados:
                print(actual, end=" ")  # Imprime el nodo actual
                visitados.add(actual)  # Agrega el nodo actual a los visitados

                # Explora los vecinos del nodo actual y los agrega a la pila si no han sido visitados
                for vecino in self.adyacencia[actual]:
                    if vecino not in visitados:
                        pila.append(vecino)

    def construir_camino(self, destino):
        # Método para construir un camino desde el nodo inicial hasta el nodo destino
        pass  # Este método aún no está implementado y necesita ser completado

# Ejemplo de uso
if __name__ == "__main__":
    adyacencia = {
        "A": ["B", "C"],
        "B": ["A", "D"],
        "C": ["A", "E"],
        "D": ["B", "F"],
        "E": ["C", "G"],
        "F": ["D"],
        "G": ["E"]
    }

    mi_grafo = Grafo(adyacencia)  # Crea una instancia de la clase Grafo con el diccionario de adyacencia
    nodo_inicio = "A"
    nodo_objetivo = "G"

    print("Recorrido en profundidad:")
    mi_grafo.profundidad(nodo_inicio)  # Realiza un recorrido en profundidad desde el nodo de inicio

    # Construye el camino desde el nodo de inicio hasta el nodo objetivo
    camino = mi_grafo.construir_camino(nodo_objetivo)  # Intenta construir un camino desde el nodo de inicio hasta el objetivo
    print("\nCamino desde A hasta G:", camino)  # Imprime el camino desde A hasta G 
