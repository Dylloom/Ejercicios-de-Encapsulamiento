class Persona:
    def __init__(self, nombre, edad, sexo):
        self._nombre = nombre
        self._edad = edad
        self._sexo = sexo

    def mostrar_informacion(self):
        return f"Nombre: {self._nombre}, Edad: {self._edad}, sexo: {self._sexo}"

    def set_edad(self, edad):
        self._edad = edad


if __name__ == "__main__":
    prueba1 = Persona("Jorge", 12, "M")
    print(prueba1.mostrar_informacion())
    prueba1.set_edad(21)
    print(prueba1.mostrar_informacion())
