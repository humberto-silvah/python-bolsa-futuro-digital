class Lampada:

    def __init__(self):

        self._ligada: False 


    def ligar(self):
        self._ligada: True
        return self._ligada
    

l1 = Lampada()
print(l1.ligar())
