class Autor:

    def __init__(self,nome, nacionalidade):
        self.__nome = nome
        self.__nacionalidade = nacionalidade

    def get_nome(self):
        return self.__nome
    
    def get_nacionalidade(self):
        return self.__nacionalidade

class Livro:

    def    __init__(self,titulo, autor: Autor):
        self.__titulo = titulo
        self.__autor = autor


    def get_titulo(self):
        return self.__titulo
    
    def get_autor(self):
        return self.__autor
    
autor1 = Autor("Machado de Assis", "Brasileiro")
livro1 = Livro("Dom Casmurro", autor1)
livro2 = Livro("Memórias Póstumas de Brás Cubas", autor1)
livro3 = Livro("Quincas Borba", autor1)
        
print(f'Título: {livro1.get_titulo()} - Autor: {livro1.get_autor().get_nome()} - Nacionalidade: {livro1.get_autor().get_nacionalidade()}')
print(f'Título: {livro2.get_titulo()} - Autor: {livro2.get_autor().get_nome()} - Nacionalidade: {livro2.get_autor().get_nacionalidade()}')
print(f'Título: {livro3.get_titulo()} - Autor: {livro3.get_autor().get_nome()} - Nacionalidade: {livro3.get_autor().get_nacionalidade()}')