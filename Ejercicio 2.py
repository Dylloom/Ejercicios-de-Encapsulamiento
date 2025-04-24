class Persona:
    def __init__(self, nombre, edad, sexo):
        self.nombre = nombre
        self.edad = edad
        self.sexo = sexo

    def mostrar_informacion(self):
        return f"Nombre: {self.nombre}, Edad: {self.edad}, Sexo: {self.sexo}"

    def cambiar_edad(self):
        
        edad = (input("Ingrese la nueva edad: "))
        self.edad = edad

# Ejemplo de uso
if __name__ == "__main__":
    Objeto = Persona("Carol", 17, "Femenino")
    print(Objeto.mostrar_informacion())
    Objeto.cambiar_edad()
    print(Objeto.mostrar_informacion())
