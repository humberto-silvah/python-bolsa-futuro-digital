class Cliente:

    def __init__(self,nome,cpf):
        self.__nome = nome
        self.__cpf = cpf


    def get_nome(self):
        return self.__nome
    
    def get_cpf(self):
        return self.__cpf
    
class ContaBancaria:
    
    def __init__(self,numero, cliente: Cliente):
        self.__numero = numero
        self.__cliente = cliente
        


    def get_numero(self):
        return self.__numero
    
    def get_cliente(self):
        return self.__cliente

cliente1 = Cliente("João Silva", "123.456.789-00")
conta1 = ContaBancaria("0001-01", cliente1)
conta2 = ContaBancaria("0001-02", cliente1)
conta3 = ContaBancaria("0001-03", cliente1) 

print(f'Conta: {conta1.get_numero()} - Cliente: {conta1.get_cliente().get_nome()} - CPF: {conta1.get_cliente().get_cpf()}')
    
   