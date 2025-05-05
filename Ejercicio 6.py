class Rectangulo:
    def __init__(self, base, altura):
        self._base = base
        self._altura = altura
       

    def calcular_area(self):
        area = self._base * self._altura
        return f"El area es {area}"

    def calcular_perimetro(self):
        perimetro = (self._base*2) + (self._altura*2)
        return f"El perimetro es: {perimetro}"
        
            
if __name__ == "__main__":
    prueba1 = Rectangulo(10, 20)
    print(prueba1.calcular_area())
    print(prueba1.calcular_perimetro())
