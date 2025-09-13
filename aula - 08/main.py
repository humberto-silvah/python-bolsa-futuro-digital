import Produto
import ContaBancaria
import Carro



conta1 = ContaBancaria("Pedro", 5000)
print(conta1.titular)
print(conta1.saldo)

conta1.depositar(2000)
conta1.sacar(1000)
conta1.exibir_saldo()


Carro1 = Carro.Carro("Fusca", 50)
print(Carro1.modelo)
print(Carro1.velocidade)
Carro1.acelerar(30)
Carro1.frear(60)
Carro1.frear(20)
Carro1.velocidade = -10