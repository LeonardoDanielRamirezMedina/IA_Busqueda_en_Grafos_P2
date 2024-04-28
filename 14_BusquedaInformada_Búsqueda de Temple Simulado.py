#   ENFOQUE:BUSQUEDA EN GRAFOS   #

# LEONARDO DANIEL RAMÍREZ MEDINA #
#        6E1   21310138          #
#        IA - 2DO PARCIAL        #

#Busqueda informada - Búsqueda de Temple Simulado

import random  # se usa para generar números aleatorios
import math  # usamos math para operaciones matemáticas

def objetivo(x):
    return x**2  # Retorna el cuadrado del valor de x

def temple_simulado():
    temperatura_inicial = 100.0  # Establece la temperatura inicial del temple simulado
    temperatura_actual = temperatura_inicial  # Inicializa la temperatura actual con la temperatura inicial
    solucion_actual = random.uniform(-10, 10)  # Genera una solución inicial aleatoria en el rango [-10, 10]

    while temperatura_actual > 1e-6:  # Bucle principal: se ejecuta mientras la temperatura actual sea mayor que 1e-6
        vecino = solucion_actual + random.uniform(-1, 1)  # Genera un vecino aleatorio sumando un valor aleatorio en el rango [-1, 1] a la solución actual
        delta = objetivo(vecino) - objetivo(solucion_actual)  # Calcula la diferencia entre el valor objetivo del vecino y el valor objetivo de la solución actual

        if delta < 0 or random.random() < math.exp(-delta / temperatura_actual):
            # Comprueba si el vecino tiene un valor objetivo menor que la solución actual o si se cumple una condición basada en la probabilidad y la diferencia de valores objetivos
            solucion_actual = vecino  # Actualiza la solución actual si se cumple alguna de las condiciones anteriores

        temperatura_actual *= 0.99  # Reduce gradualmente la temperatura actual multiplicándola por 0.99 en cada iteración

    return solucion_actual  # Devuelve la mejor solución encontrada después de que el temple simulado haya convergido

# Llama a la función temple_simulado para encontrar la mejor solución
mejor_solucion = temple_simulado()
# Imprime la mejor solución encontrada y su valor objetivo
print(f"Mejor solución encontrada: {mejor_solucion} (valor objetivo: {objetivo(mejor_solucion)})")
