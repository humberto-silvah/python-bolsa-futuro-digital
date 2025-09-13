class Produto:

    def __init__(self,nome, valor=0):
        
        self.nome = nome
        self.__valor = valor

    @property
    def valor(self):
        return self.__valor
    
    @valor.setter
    def valor(self, novo_valor):
        if novo_valor >= 0:
            self.__valor = novo_valor
        else:
            print("Valor deve ser maior ou igual a zero")
