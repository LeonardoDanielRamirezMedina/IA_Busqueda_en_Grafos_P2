#   ENFOQUE:BUSQUEDA EN GRAFOS   #

# LEONARDO DANIEL RAMÍREZ MEDINA #
#        6E1   21310138          #
#        IA - 2DO PARCIAL        #

#Utilidad y Toma de Decisiones - iteración de valores
#En busqueda en grafos la iteración de valores es un proceso que se utiliza para actualizar los valores de los nodos en un grafo.

#se define una clase para el grafo de ventas
class GrafoVentas:
    def __init__(self): #se define el constructor de la clase
        self.grafo = {}  # Diccionario para almacenar nodos y relaciones

    def agregar_cliente(self, cliente): #se define un metodo para agregar un cliente al grafo
        if cliente not in self.grafo:   #se verifica si el cliente no existe en el grafo
            self.grafo[cliente] = []    #se agrega el cliente al grafo

    def agregar_producto(self, cliente, producto):  #se define un metodo para agregar un producto a un cliente
        if cliente in self.grafo:                   #se verifica si el cliente existe en el grafo
            self.grafo[cliente].append(producto)    #se agrega el producto al cliente
        else:
            print(f"El cliente '{cliente}' no existe en el grafo.") #se imprime un mensaje de error

    def obtener_productos_por_cliente(self, cliente):   #se define un metodo para obtener los productos de un cliente
        if cliente in self.grafo:                       #se verifica si el cliente existe en el grafo
            return self.grafo[cliente]                  #se retorna la lista de productos del cliente
        else:
            return []                                   #si el cliente no existe se retorna una lista vacia

    def mostrar_grafo(self):
        for cliente, productos in self.grafo.items():       #se recorren los clientes y productos del grafo
            print(f"Cliente: {cliente}")                    #se imprime el cliente
            print(f"Productos comprados: {', '.join(productos)}")       #se imprime los productos del cliente
            print("-" * 30)                                


if __name__ == "__main__":      #se verifica si el script se ejecuta como programa principal
    ventas = GrafoVentas()      #se crea una instancia de la clase GrafoVentas 

    
    ventas.agregar_cliente("ClienteA")  
    ventas.agregar_cliente("ClienteB")
    ventas.agregar_producto("ClienteA", "Producto1")
    ventas.agregar_producto("ClienteA", "Producto2")
    ventas.agregar_producto("ClienteB", "Producto3")

    # Mostrar productos por cliente
    print("Productos comprados por ClienteA:")
    print(ventas.obtener_productos_por_cliente("ClienteA"))

    # Mostrar todo el grafo
    print("\nGrafo de ventas:")
    ventas.mostrar_grafo()      
    
