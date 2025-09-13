import Produto
import ContaBancaria
import Carro

camisa = Produto.Produto("Camisa", 79.90)
print(camisa.nome)
print(camisa.valor)
camisa.valor = 89.90
print(camisa.valor)
camisa.valor = -10

conta1 = ContaBancaria("Pedro", 5000)
print(conta1.titular)
print(conta1.saldo)
conta1.depositar(1500)
conta1.sacar(2000)
conta1.exibir_saldo()
conta1.sacar(5000)
conta1.saldo = -100


Carro1 = Carro.Carro("Fusca", 50)
print(Carro1.modelo)
print(Carro1.velocidade)
Carro1.acelerar(30)
Carro1.frear(60)
Carro1.frear(20)
Carro1.velocidade = -10