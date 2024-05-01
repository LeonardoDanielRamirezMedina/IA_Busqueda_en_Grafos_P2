#   ENFOQUE:BUSQUEDA EN GRAFOS   #

# LEONARDO DANIEL RAMÍREZ MEDINA #
#        6E1   21310138          #
#        IA - 2DO PARCIAL        #

#Utilidad y Toma de Decisiones - Redes de desición
#En busqueda en grafoslas redes dedesicion se utilizan para modelar problemas de toma de decisiones secuenciales, donde cada nodo representa un estado del sistema y cada arista representa una decisión que puede tomarse.

class Nodo:#se crea la clase nodo
    def __init__(self, nombre):
        self.nombre = nombre
        self.vecinos = {}  # Diccionario de nodos vecinos y sus costos

    def agregar_vecino(self, nodo, costo):
        self.vecinos[nodo] = costo  #agrerga un vecino con su costo

class Grafo:
    def __init__(self): #se crea el constructor
        self.nodos = {} #se crea un diccionario de nodos

    def agregar_nodo(self, nodo):
        self.nodos[nodo.nombre] = nodo  #agrega un nodo al grafo

    def buscar_camino_optimo(self, inicio, destino):
        abiertos = [(0, inicio)]  # Cola de prioridad con tuplas (costo acumulado, nodo)
        visitados = set()  # Conjunto de nodos visitados
        padres = {}  # Diccionario para rastrear los padres de cada nodo

        while abiertos:
            costo_actual, nodo_actual = abiertos.pop(0) #en esta linea se saca el primer elemento de la cola de prioridad
            visitados.add(nodo_actual)  #se agrega el nodo actual a los visitados

            if nodo_actual == destino:
                # Reconstruir el camino desde el destino hasta el inicio
                camino = []
                while nodo_actual != inicio:
                    camino.append(nodo_actual)
                    nodo_actual = padres[nodo_actual]
                camino.append(inicio)
                return list(reversed(camino))  # Se devuelve el camino en orden inverso

            for vecino, costo in nodo_actual.vecinos.items():  # Para cada vecino del nodo actual
                if vecino not in visitados:  # Si el vecino no ha sido visitado
                    nuevo_costo = costo_actual + costo  # Se calcula el nuevo costo
                    abiertos.append((nuevo_costo + self.heuristica(vecino, destino), vecino))  # Se agrega el vecino a los abiertos
                    padres[vecino] = nodo_actual  # Se establece el nodo actual como padre del vecino

        return None  # Si no se encontró un camino, se devuelve None

    def heuristica(self, nodo, destino):  # Método para calcular la heurística entre dos nodos
        # En este caso, la heurística es la distancia en línea recta entre los nodos
        return 0

# Se crean los nodos y se definen las conexiones entre ellos
nodo_a = Nodo("Entrada")
nodo_b = Nodo("Pasillo oscuro")
nodo_c = Nodo("Sala de trampas")
nodo_d = Nodo("Tesoro")

nodo_a.agregar_vecino(nodo_b, 5)
nodo_b.agregar_vecino(nodo_c, 3)
nodo_c.agregar_vecino(nodo_d, 7)

grafo = Grafo()  # Se crea un objeto de la clase Grafo
grafo.agregar_nodo(nodo_a)
grafo.agregar_nodo(nodo_b)
grafo.agregar_nodo(nodo_c)
grafo.agregar_nodo(nodo_d)

# Se busca el camino óptimo desde el nodo de inicio hasta el nodo de destino
inicio = nodo_a
destino = nodo_d
camino_optimo = grafo.buscar_camino_optimo(inicio, destino)

# Si se encontró un camino óptimo, se imprime
if camino_optimo:
    print(f"Camino óptimo desde {inicio.nombre} hasta {destino.nombre}:")
    for nodo in camino_optimo:
        print(nodo.nombre)
# Si no se encontró un camino, se imprime un mensaje
else:
    print("No se encontró un camino válido.")