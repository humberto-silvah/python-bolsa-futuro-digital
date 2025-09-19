class Time:

    def __init__(self,nome_do_time):
        self.__nome_do_time = nome_do_time

    def get_nome(self):
        return self.__nome_do_time


class Jogador:

    def __init__(self,nome, time: Time):
        self.__nome = nome
        self.__time = time

    def get_nome(self):
        return self.__nome
    
    def get_time(self):
        return self.__time
    
time1 = Time("Flamengo")
time2 = Time("Palmeiras")
jogador1 = Jogador("Gabigol", time1)
jogador2 = Jogador("Dudu", time2)
jogador3 = Jogador("Bruno Henrique", time1)

print(f'Jogador: {jogador1.get_nome()} - Time: {jogador1.get_time().get_nome()}')
print(f'Jogador: {jogador2.get_nome()} - Time: {jogador2.get_time().get_nome()}')
print(f'Jogador: {jogador3.get_nome()} - Time: {jogador3.get_time().get_nome()}')