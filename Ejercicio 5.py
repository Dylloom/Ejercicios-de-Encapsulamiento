class Estudiante:
    def __init__(self, nombre, edad):
        self._nombre = nombre
        self._edad = edad
        self._notas = []

    def agregar_nota(self):
        print("Poner las notas de 5 pruebas")
        for i in range (0, 5):
            nota = int(input("Nota a agregar: "))
            self._notas.append(nota)

    def promedio(self):
        aux=0
        tot=0
        for a in self._notas:
            aux += 1
            tot += a
        return f"El promedio es: {tot/aux}"
            
if __name__ == "__main__":
    prueba1 = Estudiante("Juan", 18)
    prueba1.agregar_nota()
    print(prueba1.promedio())
