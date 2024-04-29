#   ENFOQUE:BUSQUEDA EN GRAFOS   #

# LEONARDO DANIEL RAMÍREZ MEDINA #
#        6E1   21310138          #
#        IA - 2DO PARCIAL        #

import random

class ProblemaAsignacion:
    def __init__(self, empleados, tareas, compatibilidades):
        self.empleados = empleados                  # Lista de empleados
        self.tareas = tareas                        # Lista de tareas
        self.compatibilidades = compatibilidades    # Matriz de compatibilidad entre empleados y tareas

    def asignacion_inicial(self):
        return {tarea: random.choice(self.empleados) for tarea in self.tareas} # Genera una asignación inicial aleatoria de tareas a empleados

    def calcular_conflictos(self, asignacion):
        # Calcula el número de conflictos en la asignación actual
        conflictos = 0
        for tarea, empleado in asignacion.items():
            conflictos += 1 if not self.compatibilidades[tarea][empleado] else 0
        return conflictos

    def minimos_conflictos(self, max_iter):
        # Resuelve el problema utilizando la estrategia de mínimos conflictos
        asignacion = self.asignacion_inicial()  # Genera una asignación inicial
        for _ in range(max_iter):
            conflictos = self.calcular_conflictos(asignacion)  # Calcula los conflictos en la asignación actual
            if conflictos == 0:  # Si no hay conflictos, se ha encontrado una solución
                return asignacion
            tarea = random.choice(list(asignacion.keys()))  # Elige aleatoriamente una tarea para cambiar de empleado
            # Encuentra el empleado que minimiza los conflictos al asignarle la tarea seleccionada
            empleado_min_conflictos = min(self.empleados, key=lambda e: self.calcular_conflictos({**asignacion, tarea: e}))
            asignacion[tarea] = empleado_min_conflictos  # Asigna la tarea al empleado que minimiza los conflictos
        return None

# se asiganan tareas a los empleados
empleados = ["Juan", "María", "Pedro", "Laura", "Carlos"]       #se iniciliza la lista de empleados
tareas = ["Desarrollo", "Diseño", "Marketing", "Soporte", "Ventas"]  #se iniciliza la lista de tareas


compatibilidades = {    # Diccionario donde se establece la compatibilidad entre empleados y tareas
    "Desarrollo": {"Juan": True, "María": False, "Pedro": True, "Laura": False, "Carlos": True},
    "Diseño": {"Juan": True, "María": True, "Pedro": False, "Laura": True, "Carlos": False},
    "Marketing": {"Juan": False, "María": True, "Pedro": True, "Laura": False, "Carlos": True},
    "Soporte": {"Juan": True, "María": True, "Pedro": True, "Laura": True, "Carlos": True},
    "Ventas": {"Juan": False, "María": True, "Pedro": False, "Laura": True, "Carlos": True}
}

problema = ProblemaAsignacion(empleados, tareas, compatibilidades) # Se crea el problema de asignación

asignacion_optima = problema.minimos_conflictos(max_iter=1000)  # se resuelve el problema utilizando búsqueda local de mínimos conflictos

if asignacion_optima:       # se muestra la asignación óptima
    print("Asignación óptima de tareas a empleados:")
    for tarea, empleado in asignacion_optima.items():
        print(f"Tarea: {tarea} - Empleado: {empleado}")
else:
    print("No se encontró una asignación óptima.")
