class Estudiante:
    def __init__(self, nombre, edad, notas):
        self.nombre = nombre
        self.edad = edad
        self.notas = notas

    def mostrar_informacion(self):
        return f"Nombre: {self.nombre}, Edad: {self.edad}, Notas: {self.notas}"

    def agregar_nota(self):
        nota = float(input("Ingrese la nueva nota: "))
        self.notas.append(nota)

    def promedio(self):
        suma = sum(self.notas)  
        cantidad = len(self.notas) 
        if cantidad > 0:
            return suma / cantidad
        return 0  

if __name__ == "__main__":
    estudiante = Estudiante("Juan", 17, [4, 7, 10, 9])
    print(estudiante.mostrar_informacion())
    
    for _ in range(2):  
        estudiante.agregar_nota()
    
    print(f"El promedio es {estudiante.promedio()}")
