from Funcionario import Funcionario

class Desenvolvedor(Funcionario):
    def __init__(self, nome, bonos):
        super().__init__(nome, bonos)
        self.salario_base = self.salario_base * 2
        
    def calcular_salario(self):       
        return self.salario_base + (self.salario_base * self.bonos / 100)
    
    def __str__(self):
        return f"Desenvolvedor: {self.nome}, Salário Base: {self.salario_base}, Bonos: {self.bonos}% , Salário Total: {self.calcular_salario()}"

 