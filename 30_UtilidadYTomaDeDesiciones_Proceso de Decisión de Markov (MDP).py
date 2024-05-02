#   ENFOQUE:BUSQUEDA EN GRAFOS   #

# LEONARDO DANIEL RAMÍREZ MEDINA #
#        6E1   21310138          #
#        IA - 2DO PARCIAL        #

#Utilidad y Toma de Decisiones - Proceso de Decisión de Markov (MDP)
#el proceso de decisión de Markov (MDP) es un marco matemático para modelar la toma de decisiones secuenciales en situaciones en las que los resultados son parcialmente aleatorios y parcialmente controlables.

class MDP:
    def __init__(self):
        # se definen los estados posibles 
        self.states = ['Esperando_Tarea', 'Realizando_Tarea', 'Tarea_Completada']
        
        # se definen las acciones posibles
        self.actions = ['Recibir_Tarea', 'Realizar_Tarea', 'Entregar_Tarea']
        
        # se define la matriz de transición
        #se compone una matriz de transición que describe la probabilidad de pasar de un estado a otro dado una acción
        self.transition_matrix = {
            'Esperando_Tarea': {'Recibir_Tarea': {'Esperando_Tarea': 0.7, 'Realizando_Tarea': 0.3}, 'Realizar_Tarea': {'Esperando_Tarea': 0.9, 'Realizando_Tarea': 0.1}, 'Entregar_Tarea': {'Esperando_Tarea': 1.0}},
            'Realizando_Tarea': {'Recibir_Tarea': {'Esperando_Tarea': 0.2, 'Realizando_Tarea': 0.8}, 'Realizar_Tarea': {'Realizando_Tarea': 0.6, 'Tarea_Completada': 0.4}, 'Entregar_Tarea': {'Tarea_Completada': 1.0}},    
            'Tarea_Completada': {'Recibir_Tarea': {'Esperando_Tarea': 0.8, 'Realizando_Tarea': 0.2}, 'Realizar_Tarea': {'Realizando_Tarea': 0.1, 'Tarea_Completada': 0.9}, 'Entregar_Tarea': {'Tarea_Completada': 1.0}}
        }
        
        # se define la matriz de recompensas
        self.rewards = {
            'Esperando_Tarea': {'Recibir_Tarea': 2, 'Realizar_Tarea': -1, 'Entregar_Tarea': 0}, #se asigna una recompensa a cada acción en cada estado
            'Realizando_Tarea': {'Recibir_Tarea': -1, 'Realizar_Tarea': 2, 'Entregar_Tarea': 5},    
            'Tarea_Completada': {'Recibir_Tarea': -1, 'Realizar_Tarea': 0, 'Entregar_Tarea': 10}
        }

    

# Crear un objeto MDP que cumple la función de un proceso de decisión de Markov
mdp = MDP()
print("Espacio Estatal:", mdp.states)   #imprimir los estados posibles
print("Espacio de Acción:", mdp.actions)    #imprimir las acciones posibles
print("Matriz de Transición:", mdp.transition_matrix)   #imprimir la matriz de transición
print("Recompensas:", mdp.rewards)  #imprimir las recompensas