import random

from jogocaraacara import CaraaCara
from CaraaCara import Jogo

def menu():
    print("\033[33m-=-=-SEJA BEM VINDO AO CARA A CARA-=-=-=\033[m")
    print("\033[33m----VOCÊ TEM 3 CHANCES PARA ACERTAR-----\033[m")
    print("\033[33m------------ESCOLHA UMA OPÇÃO-----------\033[m")
    print("\033[32m[1] Lugares\n[2] Pessoas\n[3] Objetos\n[4] Sair\033[m")
    print("\033[32m----------------BOA SORTE-----------------\033[m")
    escolha_usuario = int(input("\033[36mDigite sua opção: \033[m"))
    return escolha_usuario


def jogo(escolha_usuario):
    while True:

        if escolha_usuario == 1:
            opcao_lugar()
        elif escolha_usuario == 2:
            opcao_pessoa()
        elif escolha_usuario == 3:
            opcao_objeto()
        elif escolha_usuario == 4:
            print("ATÉ MAIS!")
            quit()
        else:
            print("Digite uma opção válida!!")

def opcao_lugar():
    vida = 3
    while True:
        sorteio_lugar = Jogo.lugar_sorteado(Jogo)

        aposta_lugar_usuario = input("Digite sua aposta: ")
        if aposta_lugar_usuario == sorteio_lugar:
            print("Você ganhou!")
            escolha_usuario = input("Quer continuar? S/N").upper()
            if escolha_usuario in "Ss":
                continue
            elif escolha_usuario in "Nn":
                break
            else:
                print("Escreva S(sim) ou N(não)")
        else:
            vida -= 1
            print(f"Você errou! Suas chances são {vida}")
            if vida <=0:
                print("Suas chances acabaram! Tente novamente!")
                quit()



def opcao_pessoa():
    vida =3
    while True:
        sorteio_pessoa = Jogo.pessoa_sorteada(Jogo)
        aposta_pessoa = input("Digite sua aposta: ")
        if aposta_pessoa == sorteio_pessoa:
            print("Você ganhou!!")
            escolha_usuario = input("Quer continuar? S/N").upper()
            if escolha_usuario in "Ss":
                continue
            elif escolha_usuario in "Nn":
                break
            else:
                print("Escreva S(sim) ou N(não)")
        else:
            vida -=1
            print(f"Você errou! Suas chances são: {vida}")
            if vida <= 0:
                print("Suas chances acabaram! Tente novamente!")
                quit()


def opcao_objeto():
    vida = 3
    while True:
        sorteio_onjetoo = Jogo.objeto_sorteado(Jogo)
        aposta_objeto = input("Digite sua aposta: ")
        if aposta_objeto == sorteio_onjetoo:
            print("Você ganhou!!")
            escolha_usuario = input("Quer continuar? S/N").upper()
            if escolha_usuario in "Ss":
                continue
            elif escolha_usuario in "Nn":
                break
            else:
                print("Escreva S(sim) ou N(não)")
        else:
            vida -= 1
            print(f"Você errou! Suas chances são: {vida}")
            if vida <= 0:
                print("Suas chances acabaram! Tente novamente!")
                quit()


jogo(menu())



