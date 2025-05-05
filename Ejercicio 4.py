class Libro:
    def __init__(self, titulo, autor, año_publicacion):
        self._titulo = titulo
        self._autor = autor
        self._año_publicacion = año_publicacion

    def descripcion(self):
        return f"Titulo: {self._titulo}, Autor: {self._autor}, Año de publicacion: {self._año_publicacion}"

    def clasico(self):
        if self._año_publicacion <= (2025-50):
            return "Es un clasico"
        else:
            return "No es un clasico"
    

if __name__ == "__main__":
    prueba1 = Libro("Sistema 5-1", "Yuji Nishida", 2023)
    print(prueba1.descripcion())
    print(prueba1.clasico())
