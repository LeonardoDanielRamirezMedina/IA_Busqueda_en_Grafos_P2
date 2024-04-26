#   ENFOQUE:BUSQUEDA EN GRAFOS   #

# LEONARDO DANIEL RAMÍREZ MEDINA #
#        6E1   21310138          #
#        IA - 2DO PARCIAL        #

#Busqueda informada - Búsqueda Voraz Primero el Mejor

def busqueda_voraz_primero_el_mejor(ciudades, inicio, objetivo, heuristica):
    # se inicializa la fila de prioridad con la ciudad inicial y costo 0
    abiertos = [(inicio, 0)]
    cerrados = set()  # se crea un conjunto para guardar las ciudades ya exploradas

    while abiertos:
        actual, _ = abiertos.pop(0)  # Obtener la ciudad con el valor heurístico más bajo
        if actual == objetivo:
            return True  # regresa el valor true si se encuentra el objetivo
        cerrados.add(actual)  # se agrega la ciudad actual a las exploradas

        # ciclo para explorar los vecinos de la ciudad actual
        for vecino in ciudades[actual]:
            if vecino not in cerrados:  # si no ha sido explorado el vecino entonces se realiza lo siguiente
                valor_h = heuristica[vecino]  # se obtiene el valor heurístico del vecino
                abiertos.append((vecino, valor_h))  # se agraga a la cola de prioridad
                abiertos.sort(key=lambda x: x[1])  # se ordena por valor heurístico

    return False  # Objetivo no encontrado

#Se inicializa el grafo en el que se aplicara la busqueda
ciudades = {
    'Tokio': ['Kioto', 'Osaka'],
    'Kioto': ['Tokio', 'Osaka'],
    'Osaka': ['Tokio', 'Kioto'],
    'Nueva York': ['Los Ángeles', 'Chicago'],
    'Los Ángeles': ['Nueva York', 'Chicago'],
    'Chicago': ['Nueva York', 'Los Ángeles']
}

#se asignan los valores heuristicos
valores_heuristicos = {
    'Tokio': 10,
    'Kioto': 8,
    'Osaka': 6,
    'Nueva York': 12,
    'Los Ángeles': 9,
    'Chicago': 7
}

ciudad_inicio = 'Tokio'     #declaranmos en que ciudad comenzara la busqueda
ciudad_objetivo = 'Kioto'   #declaramos el objetivo que buscamos

# Llamamos a la funcion de busqueda
resultado = busqueda_voraz_primero_el_mejor(ciudades, ciudad_inicio, ciudad_objetivo, valores_heuristicos)
if resultado:
    print(f"¡Objetivo '{ciudad_objetivo}' encontrado!")
else:
    print(f"Objetivo '{ciudad_objetivo}' no encontrado.")
