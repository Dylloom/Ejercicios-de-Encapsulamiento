class Juego:
    def __init__(self, nombre, genero, precio):
        self._nombre = nombre
        self._genero = genero
        self._precio = precio
       
    def informacion(self):
        return f"Nombre: {self._nombre}, Genero: {self._genero}, Precio: {self._precio}$"

    def oferta(self):
        if self._precio < 60:
            descuento = 60 - self._precio 
            return f"El juego esta en oferta tiene un descuento de {descuento}$"
        else:
            return f"El juego no esta en oferta"

    
if __name__ == "__main__":
    prueba1 = Juego("Sonic", "Accion", 50)
    print(prueba1.oferta())
    print(prueba1.informacion())
