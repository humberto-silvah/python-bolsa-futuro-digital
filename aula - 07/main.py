from carro import Carro
from pessoa import Pessoa

meu_carro = Carro("Toyota", 2016)
print(meu_carro.inf_marca())
print(meu_carro.inf_ano(),"\n")


aluno = Pessoa("Fulano",25)
aluno.apresentar()
print()