class Carro:

    def __init__(self,modelo,velocidade=0):
        
        self.modelo = modelo
        self.__velocidade = velocidade

    @property
    def velocidade(self):
        return self.__velocidade
    
    @velocidade.setter
    def velocidade(self, nova_velocidade):
        if nova_velocidade >= 0:
            self.__velocidade = nova_velocidade
        else:
            print("Velocidade deve ser maior ou igual a zero")

    def acelerar(self, incremento):
        if incremento > 0:
            self.__velocidade += incremento
            print(f"O carro acelerou {incremento} km/h. Velocidade atual: {self.__velocidade} km/h")
        else:
            print("Incremento deve ser positivo.")

    def frear(self, decremento):
        if 0 < decremento <= self.__velocidade:
            self.__velocidade -= decremento
            print(f"O carro freou {decremento} km/h. Velocidade atual: {self.__velocidade} km/h")
        else:
            print("Decremento inválido ou maior que a velocidade atual.")