class Aluno:
    def __init__(self, nome, idade ,nota):
        self.nome = nome
        self.idade = idade
        self.__nota = nota

   
    @property
    def nota(self):
        return self.__nota
    @nota.setter
    def nota(self, nova_nota):
        if 0 <= nova_nota <= 10:
            self.__nota = nova_nota
        else:
            print("Nota deve estar entre 0 e 10")  

    def apresentar(self):
        print(f"Nome: {self.nome}, Idade: {self.idade}, Nota: {self.nota}")