import random
import jogo
from jogo import Jogo


def opcao_pessoa():

        while True:

                pessoa = Jogo("Keven")
                pessoa.add_dicas('o mais lindo', "gatão", "lindo", " veio de Salvador", "toca violão")

                pessoa2 = Jogo("Manuela")
                pessoa2.add_dicas("Estuda no IF", "a melhor front-end", "melhor pessoa", "Ama Java", "Mora em uma cidade pequena")

                pessoa3 = Jogo("Pedro")
                pessoa3.add_dicas("U melhor em python", "o mais gente boa", "Tem uma aparência com Temóteo", "Está no ensino médio", "O mais novo da sala")

                lista = [pessoa.nome, pessoa2.nome, pessoa3.nome]
                escolha = random.choice(lista)

                if escolha == pessoa3.nome:
                     print(pessoa3.inicio_jogo)

                elif escolha == pessoa2.nome:
                     print(pessoa2.inicio_jogo)

                elif escolha == pessoa.nome:
                     print(pessoa.inicio_jogo)

def opcao_lugares():
    while True:
        Maranhao = Jogo("Maranhao")
        Maranhao.add_dicas('Parque nacional Lençóis freáticos', "Palácio dos leões", "Catedral Metropolitana Nossa Senhora da Vitória",
                           "Parque Nacional da Chapadas da mesa", "Capital São Luis")

        Bahia = Jogo("Bahia")
        Bahia.add_dicas("Elevador Lacerda", "Basilica Senhor do Bonfim", "Mercado Modelo", "Pelourinho",
                          "Salvador")

        Sao_Paulo = Jogo("Sao Paulo")
        Sao_Paulo.add_dicas("Parque Ibirapuera", "Mercado Municipal", "Pinacoteca",
                          "Museu do futebol", "Campinas faz parte")

        lista = [Maranhao.nome, Bahia.nome, Sao_Paulo.nome]
        escolha = random.choice(lista)

        if escolha == Maranhao.nome:
            print(Maranhao.inicio_jogo)

        elif escolha == Bahia.nome:
            print(Bahia.inicio_jogo)

        elif escolha == Sao_Paulo.nome:
            print(Sao_Paulo.inicio_jogo)


def menu():
    print("\033[41m-=-=-SEJA BEM VINDO AO JOGO CARA A CARA=--=-=\033[m")
    print("---------REGRAS: VOCÊ TEM 5 CHANCES----------")
    print("[1] Lugares\n[2] Pessoas")
    print("-"*45)
    escolha_usuario = int(input("\033[31mDigite o modo de jogo: \033[m"))
    if escolha_usuario == 1:
        opcao_lugares()
    elif escolha_usuario == 2:
        opcao_pessoa()

menu()











