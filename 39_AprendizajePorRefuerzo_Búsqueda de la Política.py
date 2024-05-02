#   ENFOQUE:BUSQUEDA EN GRAFOS   #

# LEONARDO DANIEL RAMÍREZ MEDINA #
#        6E1   21310138          #
#        IA - 2DO PARCIAL        #
#Aprendizaje Por Refuerzo - Búsqueda de la Política

#La busqueda de la política es un problema de optimización que consiste en encontrar la mejor secuencia de acciones que maximice una recompensa acumulada en un entorno dado.

class Proyecto: #se crea la clase Proyecto
    def __init__(self, nombre, costo, impacto): #se inicializa la clase con los atributos nombre, costo e impacto
        self.nombre = nombre
        self.costo = costo
        self.impacto = impacto

def buscar_politica_optima(proyectos, presupuesto): #se crea la función buscar_politica_optima que recibe como parámetros una lista de proyectos y un presupuesto
    cola = [(proyectos[0], [proyectos[0]], proyectos[0].impacto)]   #se inicializa la cola con el primer proyecto, su impacto y su costo
    mejor_politica = None   #se inicializa la mejor política como nula
    mejor_impacto = 0   #se inicializa el mejor impacto como 0

    while cola:
        proyecto_actual, camino, impacto_actual = cola.pop(0)   #se obtiene el proyecto actual, el camino actual y el impacto actual de la cola
        for vecino in proyecto_actual.vecinos:  
            nuevo_camino = camino + [vecino]    #se crea un nuevo camino con el proyecto actual y su vecino
            nuevo_impacto = impacto_actual + vecino.impacto  #se calcula el nuevo impacto sumando el impacto actual y el impacto del vecino
            if vecino.costo <= presupuesto and nuevo_impacto > mejor_impacto:   #si el costo del vecino es menor o igual al presupuesto y el nuevo impacto es mayor al mejor impacto
                mejor_politica = nuevo_camino   #la mejor política es el nuevo camino
                mejor_impacto = nuevo_impacto   #el mejor impacto es el nuevo impacto
                cola.append((vecino, nuevo_camino, nuevo_impacto))  #se agrega el vecino, el nuevo camino y el nuevo impacto a la cola

    return mejor_politica   #se retorna la mejor política

#Se crean los proyectos A, B y C con sus respectivos costos e impactos
proyecto_a = Proyecto("A", costo=10, impacto=20)
proyecto_b = Proyecto("B", costo=15, impacto=25)
proyecto_c = Proyecto("C", costo=8, impacto=18)

proyecto_a.vecinos = [proyecto_b, proyecto_c]   #se asignan los vecinos de los proyectos
proyecto_b.vecinos = [proyecto_a]   
proyecto_c.vecinos = [proyecto_a]

proyectos = [proyecto_a, proyecto_b, proyecto_c]    #se crea una lista con los proyectos
presupuesto_total = 20  #se define el presupuesto total

politica_optima = buscar_politica_optima(proyectos, presupuesto_total)  #se busca la política óptima
if politica_optima: 
    print(f"Política óptima: {' -> '.join(p.nombre for p in politica_optima)}")  #se imprime la política óptima
else:
    print("No se encontró una política dentro del presupuesto.")    #si no se encuentra una política dentro del presupuesto se imprime un mensaje

