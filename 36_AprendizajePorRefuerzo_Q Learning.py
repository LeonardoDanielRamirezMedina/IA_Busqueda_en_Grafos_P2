#   ENFOQUE:BUSQUEDA EN GRAFOS   #

# LEONARDO DANIEL RAMÍREZ MEDINA #
#        6E1   21310138          #
#        IA - 2DO PARCIAL        #
#Aprendizaje Por Refuerzo - Q-Learning

# Q-Learning es un algoritmo de aprendizaje por refuerzo que aprende una función de valor de acción que denota la calidad de una acción en un estado dado.

import numpy as np

#se define el laberinto
laberinto = np.array([[0, 1, 1, 0, 0],
                      [1, 0, 1, 1, 0],
                      [1, 1, 0, 1, 1],
                      [0, 1, 1, 0, 1],
                      [0, 0, 1, 1, 0]])

# Inicializa los Q-Values en 0
num_nodos = len(laberinto)  #Se usa len para obtener la longitud de la matriz
q_values = np.zeros((num_nodos, num_nodos)) #Se usa np.zeros para inicializar la matriz con ceros

# Define el nodo objetivo (salida del laberinto)
nodo_salida = 4

# Hiperparámetros - son valores que se utilizan para controlar el proceso de aprendizaje
alpha = 0.1  # Tasa de aprendizaje
gamma = 0.9  # Factor de descuento

# Ejecuta el algoritmo Q-Learning
for _ in range(1000): 
    estado_actual = np.random.randint(num_nodos)  # Estado inicial
    while True:
        acciones_posibles = np.where(laberinto[estado_actual] == 1)[0]  # Acciones posibles
        siguiente_estado = np.random.choice(acciones_posibles)  # Acción aleatoria
        recompensa = 1 if siguiente_estado == nodo_salida else 0  # Recompensa (1 si llegamos a la salida)
        q_values[estado_actual, siguiente_estado] = (1 - alpha) * q_values[estado_actual, siguiente_estado] + \
                                                   alpha * (recompensa + gamma * np.max(q_values[siguiente_estado]))
        estado_actual = siguiente_estado    # Actualiza el estado actual con el siguiente estado
        if estado_actual == nodo_salida:
            break   # Si llegamos a la salida, termina el ciclo

# Encuentra la ruta óptima
estado_actual = 0  # Estado inicial
ruta_optima = [estado_actual]   # Ruta óptima
while estado_actual != nodo_salida: # Mientras no lleguemos a la salida
    siguiente_estado = np.argmax(q_values[estado_actual])   # Siguiente estado
    ruta_optima.append(siguiente_estado)    # Añade el siguiente estado a la ruta óptima
    estado_actual = siguiente_estado    # Actualiza el estado actual con el siguiente estado

    print("Ruta óptima:", ruta_optima)  # Imprime la ruta óptima

