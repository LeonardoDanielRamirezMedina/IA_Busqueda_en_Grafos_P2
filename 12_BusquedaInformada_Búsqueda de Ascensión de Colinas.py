#   ENFOQUE:BUSQUEDA EN GRAFOS   #

# LEONARDO DANIEL RAMÍREZ MEDINA #
#        6E1   21310138          #
#        IA - 2DO PARCIAL        #

#Busqueda informada - Búsqueda de Ascensión de Colinas

class Grafo:
    def __init__(self, vertices):
        self.vertices = vertices  # Inicializa el número de vértices en el grafo
        self.lista_adyacencia = [[] for _ in range(vertices)]  # Inicializa una lista de adyacencia vacía para cada vértice

    def agregar_arista(self, u, v):
        self.lista_adyacencia[u].append(v)  # agrega aristas del vertice U al V

    def hill_climbing(self, vertice_inicial):
        vertice_actual = vertice_inicial  # Inicializa el vértice actual con el vértice inicial
        while True:
            mejor_vecino = None  # Inicializa la variable para almacenar el mejor vecino encontrado
            mejor_valor = float('-inf')  # Inicializa el mejor valor encontrado con el valor negativo infinito

            for vecino in self.lista_adyacencia[vertice_actual]:
                valor_vecino = self.funcion_objetivo(vecino)  # Calcula el valor de la función objetivo para el vecino actual
                if valor_vecino > mejor_valor:
                    mejor_valor = valor_vecino  # se actualiza el mejor valor encontrado
                    mejor_vecino = vecino  # se actualiza el mejor vecino encontrado

            if mejor_valor <= self.funcion_objetivo(vertice_actual):
                break  # si no encuentra un valor mejor acaba el algoritmo
            vertice_actual = mejor_vecino  # Actualiza el vértice actual con el mejor vecino encontrado

        return vertice_actual  # Devuelve el vértice que maximiza la función objetivo

    def funcion_objetivo(self, vertice):
        return vertice ** 2  # Retorna el cuadrado del valor del vértice

# Ejemplo de uso
grafo_ejemplo = Grafo(6)  # Crea una instancia de la clase Grafo con 6 vértices
grafo_ejemplo.agregar_arista(0, 1)  # Se agragan aristas
grafo_ejemplo.agregar_arista(0, 2)  
grafo_ejemplo.agregar_arista(1, 3) 
grafo_ejemplo.agregar_arista(2, 4)  
grafo_ejemplo.agregar_arista(3, 5)  

vertice_inicial = 2  # 2 es el valor en dinde iniciaremos la busqueda
resultado = grafo_ejemplo.hill_climbing(vertice_inicial)  # Ejecuta el algoritmo para encontrar el vértice que maximiza la función
print(f"El valor del vértice que maximiza la función es aproximadamente: {resultado}")  # Imprime el resultado obtenido
