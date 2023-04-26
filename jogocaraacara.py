
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
    def inicio_jogo(self):
        while True:
            usuario = input("Digite sua aposta: ")
            if usuario != self.__nome:
                self.__vida-=1
                return self.__vida

    def print(self):
        print(self.nome, self.add_dicas())

