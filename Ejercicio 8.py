class Producto:
    def __init__(self, nombre, precio, stock):
        self._nombre = nombre
        self._precio = precio
        self._stock = stock
       
    def aumentar_stock(self):
        aumento = int(input("Cuanto quiere aumentar el stock: "))
        self._stock += aumento

    def disminuir_stock(self):
        disminucion = int(input("Cunato quiere disminuir el stock: "))
        if disminucion <= self._stock:
            self._stock -= disminucion
        else:
            print("La cantidad a disminuir es mayor que el stock del producto")
            
if __name__ == "__main__":
    prueba1 = Producto("Mandarina", 100, 200)
    prueba1.aumentar_stock()
    prueba1.disminuir_stock()
