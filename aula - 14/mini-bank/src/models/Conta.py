from models.Historico import Historico
from models.Saque import Saque
from models.Deposito import Deposito

class Conta:
    def __init__(self, numero, cliente):
        self._saldo = 0
        self._numero = numero
        self._agencia = "0001"
        self._cliente = cliente
        self._historico = Historico()
        

    @classmethod
    def nova_conta(cls, cliente, numero):
        return cls(numero, cliente)

    @property
    def saldo(self):
        return self._saldo

    @property
    def numero(self):
        return self._numero

    @property
    def agencia(self):
        return self._agencia

    @property
    def cliente(self):
        return self._cliente

    @property
    def historico(self):
        return self._historico

    def sacar(self, valor): #implementar
        if (self.saldo >= 0) and (valor >= 0):
            self._saldo -= valor
            print("\n=== Saque realizado com sucesso! ===")
        else:
            print("\n@@@ Operação falhou! O valor informado é inválido. @@@")
            return False
        
        return False

    def depositar(self, valor):
        if valor > 0:
            self._saldo += valor
            print("\n=== Depósito realizado com sucesso! ===")
        else:
            print("\n@@@ Operação falhou! O valor informado é inválido. @@@")
            return False

        return True
    
    def realizar_transacao(self, Transacao): #implementar
        if isinstance(Transacao, Saque):
            sucesso_transacao = self.sacar(Transacao.valor)
        elif isinstance(Transacao, Deposito):
            sucesso_transacao = self.depositar(Transacao.valor)
        else:
            print("\n@@@ Operação falhou! Tipo de transação inválida. @@@")
            return False
        if sucesso_transacao:
            self.historico.adicionar_transacao( {
                "tipo": Transacao.__class__.__name__,
                "valor": Transacao.valor,
                "data": Transacao.data.strftime("%d-%m-%Y %H:%M:%S")
            } )
            return True
        return False
        
   