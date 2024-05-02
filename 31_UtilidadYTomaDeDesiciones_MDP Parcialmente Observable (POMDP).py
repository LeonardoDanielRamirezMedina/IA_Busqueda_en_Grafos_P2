#   ENFOQUE:BUSQUEDA EN GRAFOS   #

# LEONARDO DANIEL RAMÍREZ MEDINA #
#        6E1   21310138          #
#        IA - 2DO PARCIAL        #

#Utilidad y Toma de Decisiones - MDP Parcialmente Observable (POMDP)
#En un POMDP, el agente no conoce el estado real del sistema, sino que recibe observaciones que le permiten inferir el estado actual.

import numpy as np

# Definición del grafo del laberinto (representado como una matriz de adyacencia)
grafo = np.array([[0, 1, 0, 0],
                  [1, 0, 1, 1],
                  [0, 1, 0, 1],
                  [0, 1, 1, 0]])

# Creencia inicial sobre el estado actual (probabilidad de estar en cada habitación)
habitacion_actual = 0

# Probabilidades de observación (probabilidad de observar la habitación correcta)
probabilidades_observacion = np.array([0.75, 0.25, 0.5, 0.5])

# Recompensas por cada habitación (recompensa por visitar cada habitación)
recompensas = np.array([0, 0, 0, 10])

# Realizar la búsqueda en el grafo
for _ in range(10):  
    # Actualizamos la creencia sobre la habitación actual
    creencia = probabilidades_observacion[habitacion_actual] #creencia es la probabilidad de estar en la habitación actual

    # Calculamos el valor esperado de las acciones posibles
    valores_esperados = []  # Lista para almacenar los valores esperados de las acciones
    for siguiente_habitacion in range(len(grafo)):  #en las siguientes líneas se calcula el valor esperado de las acciones posibles
        if grafo[habitacion_actual, siguiente_habitacion] == 1: 
            valor_esperado = creencia * recompensas[siguiente_habitacion]   
            valores_esperados.append(valor_esperado)
        else:
            valores_esperados.append(-np.inf)  # Si no es posible moverse a la siguiente habitación, asignamos un valor muy bajo

    # Elegimos la acción con el valor esperado máximo
    mejor_accion = np.argmax(valores_esperados)

    # Movemos a la siguiente habitación
    habitacion_actual = mejor_accion    

print("Habitación final:", habitacion_actual)  # se imprime la habitación final
print("Recompensa final:", recompensas[habitacion_actual])  #se imprime la recompensa final
