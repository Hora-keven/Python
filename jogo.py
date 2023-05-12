import random

import pokemons
Pokemons = pokemons


class Jogo:
    def __init__(self):
        self.Charmeleon = Pokemons.Pokemon_fogo("Charmeleon", 64, 80, 58)
        self.Wartortle = Pokemons.Pokemon_agua("Wartortle", 63, 58, 59)
        self.Venusaur = Pokemons.Pokemon_planta("Venusaur", 82, 80, 80)
        self.comeca_jogo()
        self.dano()

    def dano(self):
        dano_critico = 30
        dano_moderado = 20
        dano_facil = 10
        self.dano_de_vida = [dano_critico, dano_moderado, dano_facil]
        escolha_dano = random.choice(self.dano_de_vida)
        return escolha_dano

    def comeca_jogo(self):

            self.lista = [self.Venusaur.nome, self.Wartortle.nome, self.Charmeleon.nome]
            self.escolha_computador = random.choice(self.lista)
            print(self.escolha_computador)

            self.usuario = input("Escolha seu Pokemon: ").title()

            # if self.usuario == self.Charmeleon.nome and self.escolha_computador == self.Wartortle.nome:
            #     self.inicio_jogo()
            #
            # elif self.escolha_computador == self.Charmeleon.nome and self.usuario == self.Charmeleon.nome:
            #     lista = [self.escolha_computador, self.usuario]
            #     self.escolha_inicio = random.choice(lista)
            #
            #     if self.escolha_inicio == self.escolha_computador:
            #
            #
            #
            # elif self.escolha_computador == self.Wartortle.nome and self.usuario == self.Wartortle.nome:
            #     self.inicio_jogo()

            # else:
            #     print("ERROOOO")

    def inicio_jogo(self):
        while True:
            print("COMEÇANDO A BATALHA!")
            if self.escolha_computador == self.Charmeleon.nome and self.usuario == self.Wartortle.nome:
                self.Charmeleon.vida -= self.dano()
                print(f"O {self.usuario} atacou! eu tenho { self.Charmeleon.vida} de vida! ")

            elif self.escolha_computador == self.Charmeleon.nome and self.usuario == self.Venusaur.nome:
                self.Venusaur.vida -= self.dano()
                print(f"O {self.escolha_computador} atacou! {self.usuario} tem {self.Venusaur.vida} de vida! ")

            elif self.escolha_computador == self.Venusaur.nome and self.usuario == self.Wartortle.nome:
                self.Wartortle.vida -= self.dano()
                print(f"O {self.escolha_computador} atacou! {self.usuario} tem {self.Wartortle.vida} de vida!")

            elif self.usuario == self.Charmeleon.nome and self.escolha_computador == self.Wartortle.nome:
                self.Charmeleon.vida -= self.dano()
                print(f"O {self.escolha_computador} atacou! {self.usuario} tem {self.Charmeleon.vida} de vida! ")

            elif self.usuario == self.Venusaur.nome and self.escolha_computador == self.Wartortle.nome:
                self.Wartortle.vida -= self.dano()
                print(f"O {self.usuario} atacou! {self.escolha_computador} tem {self.Wartortle.vida} de vida!")

            elif self.usuario == self.Venusaur.nome and self.escolha_computador == self.Venusaur








t = Jogo()
t.inicio_jogo()





    # def inicio_jogo(self):











