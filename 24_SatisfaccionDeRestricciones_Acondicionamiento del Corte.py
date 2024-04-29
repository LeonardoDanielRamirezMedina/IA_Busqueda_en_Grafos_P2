#   ENFOQUE:BUSQUEDA EN GRAFOS   #

# LEONARDO DANIEL RAMÍREZ MEDINA #
#        6E1   21310138          #
#        IA - 2DO PARCIAL        #

#Satisfacción de Restricciones -Acondicionamiento del corte

class GrafoMagico:
    def __init__(self):
        self.grafo = {}  # Diccionario para almacenar la lista de adyacencia

    def agregar_lugar(self, lugar):     #se agreaga un lugar al grafo
        if lugar not in self.grafo:
            self.grafo[lugar] = []  # Inicializa la lista de adyacencia del lugar si no existe

    def agregar_camino(self, lugar1, lugar2):   #se agrga un arista entre dos nodos
        if lugar1 in self.grafo and lugar2 in self.grafo:
            self.grafo[lugar1].append(lugar2)  # Agrega lugar2 a la lista de adyacencia de lugar1
            self.grafo[lugar2].append(lugar1)  # Agrega lugar1 a la lista de adyacencia de lugar2

    def buscar_camino_corto(self, inicio, destino):  #Encuentra el camino más corto usando el Acondicionamiento del Corte.
        visitados = set()  # Conjunto para almacenar los lugares visitados
        cola = [(inicio, [inicio])]  # Cola para el recorrido de busqueda en anchura

        while cola:
            lugar_actual, camino_actual = cola.pop(0)  # Sacamos el primer elemento de la cola

            if lugar_actual == destino:  # Si llegamos al destino se retorna el camino actual
                return camino_actual

            visitados.add(lugar_actual)  # Agregamos el lugar actual a los visitados

            for vecino in self.grafo[lugar_actual]:  # Exploramos los vecinos del lugar actual
                if vecino not in visitados:  # Si el vecino no ha sido visitado
                    cola.append((vecino, camino_actual + [vecino]))  # Agregamos el vecino a la cola con el camino actualizado
        return None  # No se encontró un camino

# Creemos nuestro bosque mágico
bosque = GrafoMagico()
bosque.agregar_lugar("Claro de las Hadas")  # Se agrgan lugares al grafo
bosque.agregar_lugar("Cascada de los Sueños")   # Se agrgan lugares al grafo
bosque.agregar_lugar("Bosque de las Luciérnagas")   # Se agrgan lugares al grafo
bosque.agregar_lugar("Árbol de los Deseos") # Se agrgan lugares al grafo

# Conectemos los lugares
bosque.agregar_camino("Claro de las Hadas", "Cascada de los Sueños")  # Agregamos un camino entre dos lugares
bosque.agregar_camino("Cascada de los Sueños", "Bosque de las Luciérnagas") # Agregamos un camino entre dos lugares
bosque.agregar_camino("Bosque de las Luciérnagas", "Árbol de los Deseos")   # Agregamos un camino entre dos lugares

# Encontremos el camino más corto
inicio = "Claro de las Hadas"
destino = "Árbol de los Deseos"
camino_corto = bosque.buscar_camino_corto(inicio, destino)

if camino_corto:
    print(f"Camino más corto desde {inicio} hasta {destino}:")
    print(" -> ".join(camino_corto))  # Imprime el camino más corto
else:
    print(f"No hay camino desde {inicio} hasta {destino}")   # se muestra este mensaje si no se encuentra un camino.
