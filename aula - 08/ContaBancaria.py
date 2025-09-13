class ContaBancaria:

    def __init__(self, titular, saldo=0):

        self.titular = titular
        self.__saldo = saldo

    @property
    def saldo(self):
        return self.__saldo
    
    @saldo.setter
    def saldo(self,novo_saldo):
        if (novo_saldo >=0):
            self.__saldo = novo_saldo
        else:
            print("Valor deve ser maior que zero")

    def depositar(self, valor):
        if valor > 0:
            self.__saldo += valor
            print(f"Depósito de R${valor} realizado com sucesso.")
        else:
            print("Valor de depósito deve ser positivo.")

    def sacar(self, valor):
        if 0 < valor <= self.__saldo:
            self.__saldo -= valor
            print(f"Saque de R${valor} realizado com sucesso.")
        else:
            print("Saldo insuficiente ou valor inválido.") 

    def exibir_saldo(self):
        print(f"Saldo atual: R${self.__saldo}")
        