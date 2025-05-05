class Empleado:
    def __init__(self, nombre, salario, departamento):
        self._nombre = nombre
        self._salario = salario
        self._departamento = departamento
       
    def aumentar_salario(self):
        aumento = float(input("Ingrese el porcentaje del aumento: "))
        salario = self._salario
        aumento = aumento/100
        incremento = salario*aumento
        self._salario += incremento
        return f"El aumento es de: {incremento} y el salario total es {self._salario}"
                    
    def informacion(self):
        return f"Nombre: {self._nombre}, Salario: {self._salario}, Departamento: {self._departamento}"
            
if __name__ == "__main__":
    prueba1 = Empleado("Jose", 100, "Finanzas")
    print(prueba1.aumentar_salario())
    print(prueba1.informacion())
