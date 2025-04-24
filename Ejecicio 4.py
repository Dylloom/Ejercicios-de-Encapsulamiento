class Libro:
    def __init__(self, titulo, autor, año_publicacion):
        self.titulo = titulo
        self.autor = autor
        self.año_publicacion = año_publicacion

    def mostrar_informacion(self):
        return f"Titulo: {self.titulo}, autor: {self.autor}, Numero de cuenta: {self.año_publicacion}"

    def descripcion(self):
        return "No entendi"

    def clasico(self):
        if self.año_publicacion < (2025-50):
            return f"Es un clasico"
        else:
            return f"No es un clasico"

# Ejemplo de uso
if __name__ == "__main__":
    Objeto = Libro("Biblia 2.0", "Papa dios", 2025)
    print(Objeto.mostrar_informacion())
    print(Objeto.descripcion())
    print(Objeto.clasico())
