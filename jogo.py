import random



class Jogo:
    def __init__(self, nome : str):
        self.__nome = nome
        self.__dicas = []
        self.__vida = 5


    @property
    def nome(self):
        return self.__nome

    def add_dicas(self, *dicas : str):
        for dica in dicas:
            self.__dicas.append(dica)

    @property
    def dicas(self):
        return self.__dicas

    @property
    def sorteia_dicas(self):
        dica = self.__dicas[self.sorteio()]
        return dica

    def sorteio(self)->int:
        sorteio = random.randint(0, 4)
        return sorteio

