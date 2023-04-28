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
        while True:
            return self.__dicas


    @property
    def inicio_jogo(self):

        while True:
            print("\033[36mDica: \033[m", self.__dicas[self.sorteio()])
            usuario = input("\033[32mDigite sua aposta: \033[m").title()
            if usuario != self.__nome:
                self.__vida -= 1
                print(f"Você errou, você tem {self.__vida} de vida!")
                if self.__vida <= 0:
                    print("Suas chances acabaram!  tente novamente!")
                    quit()

            elif usuario == self.__nome:
                print("Você ganhou! Parabéns!")

            escolha_usuario = input("Quer continuar? [S] ou [N]")
            if escolha_usuario in "Ss":
                continue
            elif escolha_usuario in "Nn":
                quit()
            else:
                print("Digite algo certo!")


    def sorteio(self)->int:
        sorteio = random.randint(0, 4)
        return sorteio

