class Circulo:
    def __init__(self, radio):
        self._radio = radio
       
    def area(self):
        return f"El area del circulo es: {(self._radio * 2)*3.14}"

   def perimetro(self):
       return f"El perimetro del circulo es: {2*3.14*self._radio}"

   def set_radio(self):
       radio = float(input("Ingrese el radio del circulo))
       self._radio = radio

    
if __name__ == "__main__":
    prueba1 = Circulo(0)
    prueba1.set_radio()
    print(prueba1.area())
    print(prueba1.perimetro())
    