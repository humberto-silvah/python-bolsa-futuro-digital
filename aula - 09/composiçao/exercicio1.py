class Paginas:

    def __init__(self, paginas):
        self.__paginas = paginas
        self.conteudo = [""] 

class Livro:

    def __init__(self,titulo, autor, paginas):
        self.__titulo = titulo
        self.__autor = autor
        self.paginas = Paginas(paginas)

    def get_titulo(self):
        return self.__titulo

    def get_autor(self):
        return self.__autor
    
livro1 = Livro("O senhor dos aneis", "J.R.R. Tolkien", 1000)
print(livro1.get_titulo())
print(livro1.get_autor())
print(livro1.paginas._Paginas__paginas)  # Acesso direto
