class Libro:
    def __init__(self, titulo, autor):
        """..."""
        self.titulo = titulo
        self.autor = autor
    
    def obtener_titulo(self):
        """..."""
        return str(self.titulo)
    
    def obtener_autor(self):
        """..."""
        return str(self.autor)

class Biblioteca:
    def __init__(self):
        """..."""
        self.coleccion = set()
    
    def agregar_libro(self, libro):
        """..."""
        self.coleccion.add((libro.titulo, libro.autor))
    
    def sacar_libro(self, titulo, autor):
        """..."""
        if not (titulo, autor) in self.coleccion:
            raise Exception("El libro no esta en la colección")
        self.coleccion.remove((titulo, autor))
        return f"Libro: {titulo}, Autor: {autor}"
    
    def contiene_libro(self, titulo, autor):
        """..."""
        return (titulo, autor) in self.coleccion

libro = Libro("HyP", "JK")
libro1 = Libro("La Isla M", "JCortazar")
libro2 = Libro("El tunel", "Sabato")
biblio = Biblioteca()
biblio.agregar_libro(libro)
biblio.agregar_libro(libro1)
biblio.agregar_libro(libro2)
print(biblio.contiene_libro("HyP", "JK"))
print(biblio.sacar_libro("HyP", "JK"))
print(biblio.contiene_libro("HyP", "JK"))