#   ENFOQUE:BUSQUEDA EN GRAFOS   #

# LEONARDO DANIEL RAMÍREZ MEDINA #
#        6E1   21310138          #
#        IA - 2DO PARCIAL        #

#Busqueda informada - Algoritmos Genéticos


import random  # se usa para utilizar numeros aleatorios

# se definen los datos de las personas
personas = [
    {"id": 1, "altura": 180},
    {"id": 2, "altura": 175},
    {"id": 3, "altura": 190},
]

# se definen los parametros para el algoritmo genético
tamano_poblacion = 50  # Tamaño de la población
num_generaciones = 100  # Número de generaciones
prob_mutacion = 0.1  # Probabilidad de mutación

def calcular_altura_promedio(equipo):       # Función para calcular la altura promedio de un equipo
    alturas = [persona["altura"] for persona in equipo]
    return sum(alturas) / len(equipo)

def seleccion_padres(poblacion):        # Función para seleccionar dos padres aleatorios de la población
    return random.sample(poblacion, 2)

def cruzar(padre1, padre2):     # Función para realizar el cruce (crossover) entre dos padres
    punto_cruza = random.randint(1, len(padre1) - 1)  # Punto de cruce aleatorio
    hijo1 = padre1[:punto_cruza] + padre2[punto_cruza:]  # Primer hijo
    hijo2 = padre2[:punto_cruza] + padre1[punto_cruza:]  # Segundo hijo
    return hijo1, hijo2

# Función para aplicar mutación a un equipo
def mutar(equipo):
    for i in range(len(equipo)):
        if random.random() < prob_mutacion:
            equipo[i]["altura"] += random.randint(-5, 5)  # Cambio aleatorio en la altura

# Inicialización de la población
poblacion = [random.sample(personas, len(personas)) for _ in range(tamano_poblacion)]

# Evolución de la población a lo largo de las generaciones
for _ in range(num_generaciones):
    nueva_generacion = []  # Lista para almacenar la nueva generación
    for _ in range(tamano_poblacion // 2):  # Cada par de padres generará dos hijos
        padre1, padre2 = seleccion_padres(poblacion)  # Seleccionamos dos padres
        hijo1, hijo2 = cruzar(padre1, padre2)  # Cruzamos los padres para obtener dos hijos
        mutar(hijo1)  # se aplica mutación al primer hijo
        mutar(hijo2)  # se aplica mutación al segundo hijo
        nueva_generacion.extend([hijo1, hijo2])  # Agregamos los hijos a la nueva generación
    poblacion = nueva_generacion  # Reemplazamos la población anterior con la nueva generación

# se encuentra el equipo con la altura promedio más alta
mejor_equipo = max(poblacion, key=calcular_altura_promedio)  # Buscamos el equipo con la altura promedio más alta
altura_promedio_mejor_equipo = calcular_altura_promedio(mejor_equipo)  # Calculamos la altura promedio del mejor equipo

# Imprimimos el mejor equipo encontrado junto con sus alturas
print(f"Mejor equipo (altura promedio: {altura_promedio_mejor_equipo:.2f} cm):")
for persona in mejor_equipo:
    print(f"ID {persona['id']}: {persona['altura']} cm")
