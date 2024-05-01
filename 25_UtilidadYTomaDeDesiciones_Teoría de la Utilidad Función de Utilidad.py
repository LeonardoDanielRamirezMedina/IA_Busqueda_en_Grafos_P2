#   ENFOQUE:BUSQUEDA EN GRAFOS   #

# LEONARDO DANIEL RAMÍREZ MEDINA #
#        6E1   21310138          #
#        IA - 2DO PARCIAL        #

#Utilidad y Toma de Decisiones - Teoría de la Utilidad Función de Utilidad

#En busqueda en grafos, la teoría de la utilidad es una técnica que se utiliza para tomar decisiones en situaciones donde hay incertidumbre.


class ProblemaRutas: #se crea la clase ProblemaRutas
    def __init__(self, grafo, costos, tiempos):
        #inicializa el grafo, los costos y los tiempos
        self.grafo = grafo  # Grafo de las ciudades y sus conexiones
        self.costos = costos  # Costos de viaje entre ciudades
        self.tiempos = tiempos  # Tiempos de viaje entre ciudades

    def calcular_utilidad(self, ruta):  #se crea el método calcular_utilidad
        # Método para calcular la utilidad de una ruta
        costo_total = sum(self.costos[a][b] for a, b in zip(ruta, ruta[1:]))  # Suma los costos de la ruta
        tiempo_total = sum(self.tiempos[a][b] for a, b in zip(ruta, ruta[1:]))  # Suma los tiempos de la ruta
        return -costo_total - tiempo_total  # Devuelve la utilidad como un valor negativo

    def buscar_ruta_optima(self, origen, destino):
        # Método para buscar la ruta óptima, se debe implementar el algoritmo de búsqueda
        pass  # No implementado

# Definición del grafo de las ciudades y sus conexiones
grafo = {
    "A": {"B": 10, "C": 20},
    "B": {"A": 10, "C": 15, "D": 25},
    "C": {"A": 20, "B": 15, "D": 30},
    "D": {"B": 25, "C": 30}
}

# Definición de los costos de viaje entre ciudades
costos = {
    "A": {"B": 50, "C": 70},
    "B": {"A": 50, "C": 60, "D": 80},
    "C": {"A": 70, "B": 60, "D": 90},
    "D": {"B": 80, "C": 90}
}

# Definición de los tiempos de viaje entre ciudades
tiempos = {
    "A": {"B": 2, "C": 3},
    "B": {"A": 2, "C": 2, "D": 4},
    "C": {"A": 3, "B": 2, "D": 5},
    "D": {"B": 4, "C": 5}
}

# Creación de un objeto de la clase ProblemaRutas
problema = ProblemaRutas(grafo, costos, tiempos)

# Definición del origen y destino para buscar la ruta óptima
origen = "A"
destino = "D"
ruta_optima = problema.buscar_ruta_optima(origen, destino)  # Búsqueda de la ruta óptima

# Impresión de la ruta óptima y su utilidad
if ruta_optima:
    print(f"Ruta óptima de {origen} a {destino}: {ruta_optima}")  # Imprime la ruta óptima
    utilidad = problema.calcular_utilidad(ruta_optima)  # Calcula la utilidad de la ruta óptima
    print(f"Utilidad de la ruta: {utilidad}")  # Imprime la utilidad de la ruta óptima
else:
    print("No se encontró una ruta óptima.")  # Imprime un mensaje si no se encontró una ruta óptima