from abc import ABC, abstractmethod

class Funcionario:
    def __init__(self, nome, bonos):
        self.nome = nome
        self.bonos = bonos
        self.salario_base = 1500.00
        

    @abstractmethod
    def calcular_salario(self):
        pass

