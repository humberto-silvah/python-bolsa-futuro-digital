class PlayerLista:

    def __init__(self,lista_musicas):
        self.__lista_musicas = lista_musicas

    def get_lista_musicas(self):
        return self.__lista_musicas
    

class Musica:

    def __init__(self,musica, player: PlayerLista):
        self.__musica = musica
        self.__player = player

    def get_musica(self):
        return self.__musica    
    
    def get_player(self):
        return self.__player
    
player1 = PlayerLista("Top Hits 2024")
musica1 = Musica("As It Was", player1)
musica2 = Musica("About Damn Time", player1)
musica3 = Musica("Bad Habit", player1)

print(f'Música: {musica1.get_musica()} - Player: {musica1.get_player().get_lista_musicas()}')
print(f'Música: {musica2.get_musica()} - Player: {musica2.get_player().get_lista_musicas()}')
print(f'Música: {musica3.get_musica()} - Player: {musica3.get_player().get_lista_musicas()}')
