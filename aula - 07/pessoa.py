class Pessoa:

    def __init__(self,nome: str, idade: int):
        
        self.nome: str = nome
        self.idade: int = idade

    def apresentar(self):
        print(f"Olá, meu nome é {self.nome} e tenho {self.idade} anos.")


