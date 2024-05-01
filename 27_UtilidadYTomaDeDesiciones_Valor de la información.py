#   ENFOQUE:BUSQUEDA EN GRAFOS   #

# LEONARDO DANIEL RAMÍREZ MEDINA #
#        6E1   21310138          #
#        IA - 2DO PARCIAL        #

#Utilidad y Toma de Decisiones - Valor de la Información
#En busqueda en grafos el valor de la informacion es una medida que se utiliza para evaluar la importancia de un conjunto de datos en un proceso de toma de decisiones.

# se define un diccionario con las ventas de tres categorías
ventas = {
    #el diccionario tiene tres categorias y cada categoria tiene una lista de tuplas con descuentos y cantidad de ventas
    'Electrónica': [(10, 50), (20, 30), (30, 20)],
    'Ropa': [(15, 40), (25, 25), (10, 35)],
    'Hogar': [(5, 60), (15, 40), (20, 30)]
}

# Función para calcular el Valor de la Información (VI)
def calcular_vi(categoria): #se define la funcion calcular_vi que recibe una categoria
    descuentos = ventas.get(categoria, [])                          #se obtiene la lista de descuentos para la categoria
    total_ventas = sum(cantidad for _, cantidad in descuentos)      #se calcula el total de ventas
    vi = 0                                                          #se inicializa el valor de la informacion en 0
    for descuento, cantidad in descuentos:                          #se recorren los descuentos y cantidades
        probabilidad = cantidad / total_ventas                      #se calcula la probabilidad de cada descuento
        vi += probabilidad * (descuento / 100) * total_ventas       #se calcula el valor de la informacion
    return vi               #se retorna el valor de la informacion

# Calcular el VI para cada categoría
categorias = ventas.keys()      #se obtienen las categorias del diccionario de ventas
vi_por_categoria = {categoria: calcular_vi(categoria) for categoria in categorias}   #se calcula el valor de la informacion para cada categoria       

# Imprimir los resultados
for categoria, vi in vi_por_categoria.items():          #por medio de un ciclo se recorren las categorias y sus valores de informacion
    print(f"Valor de la Información para {categoria}: {vi:.2f}")    #se imprime el valor de la informacion para cada categoria