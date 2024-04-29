#   ENFOQUE:BUSQUEDA EN GRAFOS   #

# LEONARDO DANIEL RAMÍREZ MEDINA #
#        6E1   21310138          #
#        IA - 2DO PARCIAL        #

#Satisfacción de Restricciones - Problemas de Satisfacción de Restricciones

class CSP:
    def __init__(self, variables, dominios, restricciones):
        self.variables = variables  # Lista de variables los cuales son nodos
        self.dominios = dominios    # Diccionario de dominios que son colores
        self.restricciones = restricciones  # Lista de restricciones entre las variables

    def resolver(self):
        asignacion = {}  # Inicializa una asignación vacía
        return self.backtracking(asignacion)

    def backtracking(self, asignacion):
        if len(asignacion) == len(self.variables):  # se encuentra una solucion si se todas las variables han sido asignadas
            return asignacion

        var_no_asignada = next(v for v in self.variables if v not in asignacion)  # Selecciona una variable no asignada
        for valor in self.dominios[var_no_asignada]:  # Prueba todos los valores del dominio de la variable
            if self.consistente(var_no_asignada, valor, asignacion):  # Verifica si la asignación es consistente
                asignacion[var_no_asignada] = valor  # Asigna el valor a la variable
                resultado = self.backtracking(asignacion)  # Llama recursivamente al backtracking
                if resultado:  # Si se encontró una solución, retorna la asignación
                    return resultado
                del asignacion[var_no_asignada]  # Si no se encontró una solución, deshace la asignación
        return None  # Si no se encontró una solución, retorna None

    def consistente(self, variable, valor, asignacion):
        for restriccion in self.restricciones:
            if variable in restriccion:  # Verifica si la variable es parte de la restricción
                otro_variable = restriccion[0] if restriccion[0] != variable else restriccion[1]
                if otro_variable in asignacion and asignacion[otro_variable] == valor:  # Verifica si hay conflictos con las restricciones
                    return False
        return True



if __name__ == "__main__":
    # Definición del grafo como un conjunto de nodos y aristas
    nodos = ['A', 'B', 'C', 'D', 'E']
    aristas = [('A', 'B'), ('A', 'C'), ('B', 'C'), ('B', 'D'), ('C', 'D'), ('C', 'E'), ('D', 'E')]

    # Definición de los dominios de las variables (colores)
    dominios = {'A': ['Rojo', 'Verde', 'Azul'],
                'B': ['Rojo', 'Verde', 'Azul'],
                'C': ['Rojo', 'Verde', 'Azul'],
                'D': ['Rojo', 'Verde', 'Azul'],
                'E': ['Rojo', 'Verde', 'Azul']}

    # Restricciones: Los nodos adyacentes no pueden tener el mismo color
    restricciones = [(arista, lambda x, y: x != y) for arista in aristas]

    # Creación del problema CSP
    problema = CSP(nodos, dominios, restricciones)

    # Resolución del problema
    solucion = problema.resolver()

    if solucion:
        print("Solución encontrada:")
        for variable, valor in solucion.items():
            print(f"{variable}: {valor}")
    else:
        print("No se encontró solución.")
