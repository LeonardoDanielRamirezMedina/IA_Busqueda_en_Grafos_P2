#   ENFOQUE:BUSQUEDA EN GRAFOS   #

# LEONARDO DANIEL RAMÍREZ MEDINA #
#        6E1   21310138          #
#        IA - 2DO PARCIAL        #

#Satisfacción de Restricciones - Comprobación Hacia Delante

class GrafoLaberinto:
    def __init__(self, vertices):
        self.vertices = vertices  # Número total de habitaciones en el laberinto
        self.grafo = {v: [] for v in range(vertices)}  # Inicializa un diccionario para representar el grafo

    def agregar_arista(self, u, v):
        self.grafo[u].append(v)        # Añade una arista entre los nodos u y v de manera bidireccional
        self.grafo[v].append(u)        # Añade una arista entre los nodos u y v de manera bidireccional

    def comprobacion_hacia_delante(self, actual, visitados, objetivo):
        if actual == objetivo:  # cuando llega al objetivo retorna True
            return True
        visitados.add(actual)  # Marca el nodo actual como visitado

        # Explora los vecinos del nodo actual
        for vecino in self.grafo[actual]:
            if vecino not in visitados:  # Si el vecino no ha sido visitado
                if self.comprobacion_hacia_delante(vecino, visitados, objetivo):  # Realiza una búsqueda en profundidad
                    return True  # Si se encuentra el objetivo retorna True

        return False  # Si no se encuentra el objetivo retorna False

    def buscar_tesoro(self, inicio, objetivo):
        visitados = set()  # Conjunto para rastrear los nodos visitados
        return self.comprobacion_hacia_delante(inicio, visitados, objetivo)  # Realiza una búsqueda en profundidad


# laberinto con 6 habitaciones
laberinto = GrafoLaberinto(6)
laberinto.agregar_arista(0, 1)
laberinto.agregar_arista(0, 2)
laberinto.agregar_arista(1, 3)
laberinto.agregar_arista(2, 4)
laberinto.agregar_arista(3, 5)
laberinto.agregar_arista(4, 5)

inicio = 0  # inicio de la busqueda
tesoro = 5  # objetivo de la busqueda

# Buscar el tesoro en el laberinto, en este caso en el nodo 5
if laberinto.buscar_tesoro(inicio, tesoro):
    print(f"¡Has encontrado el tesoro en la habitación {tesoro}!")
else:
    print("El tesoro sigue oculto. Sigue explorando...")
