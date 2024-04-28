#   ENFOQUE:BUSQUEDA EN GRAFOS   #

# LEONARDO DANIEL RAMÍREZ MEDINA #
#        6E1   21310138          #
#        IA - 2DO PARCIAL        #

#Busqueda informada - Búsqueda A*

class Grafo:
    def __init__(self):
        self.grafo = {}  #se inicializa un diccionario para guardar los datos del grafo 

    def agregar_arista(self, origen, destino, peso):
        if origen not in self.grafo:
            self.grafo[origen] = []  # Si el nodo de origen no está en el grafo se crea una lista vacía para almacenar sus vecinos.
        self.grafo[origen].append((destino, peso))  # Agrega una arista entre el nodo de origen y el nodo de destino con un peso dado.

    def a_estrella(self, inicio, destino):
        abiertos = [(inicio, 0)]  # Inicializa una lista de tuplas con el nodo de inicio y un costo acumulado de 0.
        cerrados = set()  # Inicializa un conjunto para almacenar nodos cerrados.

        while abiertos:
            nodo_actual, costo_acumulado = abiertos.pop(0)  # Selecciona y extrae el nodo actual de la lista de abiertos.

            if nodo_actual == destino:  # Verifica si el nodo actual es el nodo de destino.
                return costo_acumulado  # devuelve el costo acumulado, ya que es la ruta más corta.

            cerrados.add(nodo_actual)  # Agrega el nodo actual al conjunto de cerrados.

            for vecino, peso in self.grafo.get(nodo_actual, []):  # Itera sobre los vecinos del nodo actual.
                if vecino not in cerrados:  # Verifica si el vecino no está en los nodos cerrados.
                    costo_total = costo_acumulado + peso  # Calcula el costo total acumulado para llegar al vecino.
                    abiertos.append((vecino, costo_total))  # Agrega el vecino a la lista de abiertos con su costo total.

        return None  # Si no se encuentra una ruta devuelve el valor None.

grafo = Grafo()  # Crea una instancia de la clase Grafo.
grafo.agregar_arista('A', 'B', 4)  # Agrega una arista del nodo 'A' al nodo 'B' con un peso de 4.
grafo.agregar_arista('A', 'J', 15)  # Agrega una arista del nodo 'A' al nodo 'J' con un peso de 15.
grafo.agregar_arista('A', 'C', 1)  # Agrega una arista del nodo 'A' al nodo 'C' con un peso de 1.

inicio = 'A'  # definimos el nodo de inicio de la busqueda
destino = 'J'  # se deifne el nodo que será nuestro destino de busqueda
ruta_mas_corta = grafo.a_estrella(inicio, destino)  # Encuentra la ruta más corta desde el nodo de inicio hasta el nodo de destino.

if ruta_mas_corta is not None:
    print(f"La ruta más corta desde {inicio} hasta {destino} es de {ruta_mas_corta} unidades.")  # Imprime la ruta más corta si se encuentra.
else:
    print(f"No se encontró una ruta desde {inicio} hasta {destino}.")  # Imprime un mensaje si no se encuentra una ruta.
