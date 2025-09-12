class Pessoa:

    def __init__(self,nome: str, idade: int):
        
        self._nome: str = nome
        self._idade: int = idade

    def apresentar(self):
        print(f"Olá, meu nome é {self._nome} e tenho {self._idade} anos.")


