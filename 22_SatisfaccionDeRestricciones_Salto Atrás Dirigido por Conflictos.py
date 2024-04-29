#   ENFOQUE:BUSQUEDA EN GRAFOS   #

# LEONARDO DANIEL RAMÍREZ MEDINA #
#        6E1   21310138          #
#        IA - 2DO PARCIAL        #

#Satisfacción de Restricciones - Salto Atrás Dirigido por Conflictos

class EspacioExploracion:
    def __init__(self, grafo):
        self.grafo = grafo           # Grafo que representa las conexiones
        self.visitados = set()       # Conjunto para almacenar los planetas visitados durante la exploración
        self.solucion = []           # Lista para almacenar la ruta de exploración que conduce a la solución

    def resolver(self, nodo_actual):
        if self.es_solucion(nodo_actual):   # Si el nodo actual es una solución, retorna True
            return True

        for vecino in self.grafo[nodo_actual]:  # Explora los vecinos del nodo actual
            if vecino not in self.visitados:   # Verifica si el vecino no ha sido visitado
                self.visitados.add(vecino)     # Marca el vecino como visitado
                self.solucion.append(vecino)   # Agrega el vecino a la ruta de exploración

                if self.resolver(vecino):      # Llama recursivamente a resolver con el vecino como nodo actual
                    return True                # Si se encuentra una solución, retorna True

                self.visitados.remove(vecino)  # Si no se encuentra una solución, retrocede eliminando el vecino de visitados
                self.solucion.pop()            # Elimina el vecino de la ruta de exploración

        return False                           # Si no se encuentra ninguna solución, retorna False

    def es_solucion(self, nodo):
        # Define aquí tu criterio de satisfacción para la exploración espacial
        # Por ejemplo, si el nodo representa un planeta habitable
        return nodo == "PlanetaHabitableX"  # Retorna True si el nodo es el planeta habitable "PlanetaHabitableX"

if __name__ == "__main__":
    # se crea el grafo, los planetas son los nodos
    grafo_planetas = {
        "Tierra": ["Marte", "Venus"],
        "Marte": ["Jupiter", "Saturno"],
        "Venus": ["Mercurio"],
        "Jupiter": ["Saturno", "Urano"],
        "Saturno": ["Urano"],
        "Urano": ["PlanetaHabitableX"]  # El objetivo es llegar a "PlanetaHabitableX"
    }

    explorador = EspacioExploracion(grafo_planetas)
    explorador.visitados.add("Tierra")    # Comenzamos desde la Tierra
    explorador.solucion.append("Tierra")

    if explorador.resolver("Tierra"):     # Llama al método resolver desde la Tierra
        print("¡Hemos encontrado un planeta habitable!")    #se imprime mensaje cuando se encuentra el objetivo
        print("Ruta de exploración:", explorador.solucion)  # Muestra la ruta de exploración que lleva a la solución
    else:
        print("No se encontró un planeta habitable en esta exploración.")  #se muestra este mensaje cuendo se no encuentra el objetivo
