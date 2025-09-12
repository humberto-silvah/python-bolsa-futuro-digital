class Carro:

    def __init__(self,marca: str,ano: int):
    
        self._marca: str = marca
        self._ano: int = ano

    def inf_marca(self):
        return self._marca

    def inf_ano(self):
        return self._ano
    
